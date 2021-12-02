import os
import sys
from classes import *
import db_handler as db
import datetime


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class db_client(object):
    def __init__(self, username, password):
        try:
            self.username = username
            self.password = password
            self.__db_handler = db.database_handler()
            self.__connection = self.__db_handler.connect(self.username, self.password)
            self.__user_roles = self.__get_user_roles()
        except ConnectionError:
            raise ValueError("Невозможно подключиться к БД: Неверный логин или пароль")

    def __del__(self):
        try:
            self.__db_handler.close_connection()
        except ConnectionError as _ex:
            print('ОШИБКА:', _ex, sep='\n', file=sys.stderr)

    def __get_user_roles(self):
        try:
            roles_query = """
                WITH CTE_Roles (role_principal_id)  
                AS (SELECT role_principal_id 
                    FROM sys.database_role_members 
                    WHERE member_principal_id = USER_ID() 
                    UNION ALL 
                    SELECT drm.role_principal_id 
                    FROM sys.database_role_members drm INNER JOIN CTE_Roles CR 
                    ON drm.member_principal_id = CR.role_principal_id
                ) 
                SELECT USER_NAME(role_principal_id) RoleName 
                FROM CTE_Roles 
                UNION ALL 
                SELECT 'public' 
                ORDER BY RoleName"""

            roles = self.__db_handler.execute_query(roles_query)
            roles_list = []
            for row in roles:
                roles_list.append(row[0])
            return roles_list
        except Exception as _ex:
            print('get_user_roles failure', _ex, sep='\n')

    def get_user_actions(self):
        it = 1
        user_actions = dict()
        if 'all_teachers' in self.__user_roles:
            user_actions[it] = self.get_personal_info
            it += 1

        if 'department_heads' in self.__user_roles or 'hr_employees' in self.__user_roles:
            for function in (
                self.get_all_groups,
                self.get_all_teachers,
                self.get_all_students,
            ):
                user_actions[it] = function
                it += 1

        if 'hr_employees' in self.__user_roles:
            for function in (
                self.add_student,
                self.del_student,
                self.add_teacher,
                self.del_teacher,
                self.edit_department_info,
            ):
                user_actions[it] = function
                it += 1

        return user_actions

    def __get_institute_ID(self, department_name):
        try:
            select_query = """SELECT id FROM institutes WHERE short_name = ?"""
            items_tuple = (department_name,)
            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )
            return list(cursor_content)[0][0]
        except Exception:
            raise ValueError("Института с таким названием не существует")

    def __get_department_ID(self, group_name):
        try:
            select_query = """SELECT id FROM departments WHERE short_name = ? """
            items_tuple = (group_name,)
            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )

            return list(cursor_content)[0][0]
        except Exception:
            raise ValueError("Кафедры с таким названием не существует")

    def get_all_groups(self):
        try:
            print('Введите название института (краткое)')
            inst_name = input()
            inst_id = self.__get_institute_ID(inst_name)

            select_query = """
            SELECT departments.id, departments.full_name, departments.short_name, departments.student_count, institutes.full_name 
            FROM departments JOIN institutes
            ON institute_id = institutes.id
            WHERE institute_id = ?
            """

            items_tuple = (inst_id,)
            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )

            group_list = []
            for row in cursor_content:
                group_list.append(Department(*row))

            cls()
            for group in group_list:
                group.show()
                print()

        except ValueError as _ex:
            cls()
            print('Ошибка:', _ex, sep=' ')
            return

    def get_all_students(self):
        try:
            print('Введите название каферды (краткое)')
            dep_name = input()
            dep_id = self.__get_department_ID(dep_name)

            select_query = """
            SELECT gradebook_number, first_name, second_name, last_name, phone_number, birth_date, full_name
            FROM students JOIN departments 
            ON department_id = id
            WHERE department_id = ?"""

            items_tuple = (dep_id,)

            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )
            students_list = []

            for row in cursor_content:
                students_list.append(Student(*row))

            cls()
            for student in students_list:
                student.show()
                print()

        except ValueError as _ex:
            cls()
            print('Ошибка:', _ex, sep=' ')
            return

    def get_all_teachers(self):
        try:
            print("Введите название института (краткое)")
            inst_name = input()
            inst_id = self.__get_institute_ID(inst_name)

            select_query = """
            SELECT teachers.id, teachers.first_name, teachers.second_name, teachers.last_name, teachers.phone_number, institutes.full_name
            FROM teachers JOIN institutes
            ON teachers.institute_id = institutes.id
            WHERE institute_id = ?"""

            items_tuple = (inst_id,)
            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )
            teachers_list = []
            for row in cursor_content:
                teachers_list.append(Teacher(*row))

            cls()
            for teacher in teachers_list:
                teacher.show()
                print()

        except ValueError as _ex:
            cls()
            print('Ошибка:', _ex, sep=' ')
            return

    def get_personal_info(self):
        try:
            print("Введите свой ID:")
            teacher_id = int(input())

            select_query = """
            SELECT teachers.id, teachers.first_name, teachers.second_name, teachers.last_name, teachers.phone_number, institutes.full_name
            FROM teachers JOIN institutes
            ON teachers.institute_id = institutes.id
            WHERE teachers.id = ?"""

            items_tuple = (teacher_id,)
            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )

            teacher_info = None
            for row in cursor_content:
                teacher_info = Teacher(*row)

            cls()
            teacher_info.show()
            print()
        except Exception:
            cls()
            print("Ошибка:", "Преподавателя с данным ID не существует", sep=' ')
            return

    def add_student(self):
        try:
            cls()
            print("Введите данные о студенте:")
            print("Введите ФИО:")
            s_name, f_name, l_name = input().split()

            print("Введите дату рождения:")
            dob = datetime.datetime.strptime(input(), "%d.%m.%Y")

            print("Введите номер телефона:")
            ph_num = input()

            print("Введите название группы (краткое):")
            d_name = input()
            d_id = self.__get_department_ID(d_name)

            student = Student(None, f_name, s_name, l_name, ph_num, dob, d_name)
            cls()
            print("Вы ввели следующие данные:\n")
            student.show()

            insert_query = """
            INSERT INTO students(second_name, first_name, last_name, phone_number, birth_date, department_id) 
            VALUES (?, ?, ?, ?, ?, ?) """

            items_tuple = (s_name, f_name, l_name, ph_num, dob, d_id)

            print("\nПодтвердите действие [д/Н]")
            if input() == 'д':
                self.__db_handler.execute_query(
                    insert_query, items=items_tuple, commit=True
                )
            else:
                print("Действие отменено.")
                return

        except ValueError as _ex:
            cls()
            print('Ошибка:', _ex, sep=' ')
            return
        except Exception:
            cls()
            print("Проверьте правильность введенных данных")
            return
        else:
            cls()
            print("Запись о студенте успешно добавлена")
            return

    def del_student(self):
        try:
            print("Введите номер зачетной книжки студента:")
            st_id = int(input())

            select_query = """
            SELECT gradebook_number, first_name, second_name, last_name, phone_number, birth_date, full_name
            FROM students JOIN departments
            ON department_id = id
            WHERE gradebook_number = ?"""
            items_tuple = (st_id,)
            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )

            for row in cursor_content:
                student = Student(*row)

            cls()
            print("Вы хотите удалить запись о студенте:")
            student.show()

            print("\nПодтвердите действие [д/Н]")
            if input() == 'д':
                delete_query = """DELETE FROM students WHERE gradebook_number = ? """
                self.__db_handler.execute_query(
                    delete_query, items=items_tuple, commit=True
                )
            else:
                print("Действие отменено.")
                return

        except Exception:
            cls()
            print("Что-то пошло не так")
            return
        else:
            cls()
            print("Запись о студенте успешно удалена")
            return

    def add_teacher(self):
        try:
            cls()
            print("Введите данные о преподавателей:")
            print("Введите ФИО:")
            s_name, f_name, l_name = input().split()

            print("Введите номер телефона:")
            ph_num = input()

            print("Введите название института (краткое):")
            i_name = input()
            i_id = self.__get_institute_ID(i_name)

            teacher = Teacher(None, f_name, s_name, l_name, ph_num, i_name)

            cls()
            print("Вы ввели следующие данные:\n")
            teacher.show()

            insert_query = """
            INSERT INTO teachers(second_name, first_name, last_name, phone_number, institute_id) 
            VALUES (?, ?, ?, ?, ?) """

            items_tuple = (s_name, f_name, l_name, ph_num, i_id)

            print("\nПодтвердите действие [д/Н]")
            if input() == 'д':
                self.__db_handler.execute_query(
                    insert_query, items=items_tuple, commit=True
                )
            else:
                print("Действие отменено.")
                return

        except ValueError as _ex:
            cls()
            print('Ошибка:', _ex, sep=' ')
            return
        except Exception:
            cls()
            print("Проверьте правильность введенных данных")
            return
        else:
            cls()
            print("Запись о преподавателе успешно добавлена")
            return

    def del_teacher(self):
        try:
            print("Введите ID преподавателя:")
            t_id = int(input())

            select_query = """
            SELECT teachers.id, teachers.first_name, teachers.second_name, teachers.last_name, teachers.phone_number, institutes.full_name
            FROM teachers JOIN institutes 
            ON teachers.institute_id = institutes.id
            WHERE teachers.id = ?"""
            items_tuple = (t_id,)
            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )

            for row in cursor_content:
                teacher = Teacher(*row)

            cls()
            print("Вы хотите удалить запись о преподавателе:")
            teacher.show()

            print("\nПодтвердите действие [д/Н]")
            if input() == 'д':
                delete_query = """DELETE FROM teachers WHERE id = ? """
                self.__db_handler.execute_query(
                    delete_query, items=items_tuple, commit=True
                )
            else:
                print("Действие отменено.")
                return

        except Exception:
            cls()
            print("Что-то пошло не так")
            return
        else:
            cls()
            print("Запись о преподавателе успешно удалена")
            return

    def edit_department_info(self):
        try:
            print("Введите название института (краткое):")
            i_name = input()
            i_id = self.__get_institute_ID(i_name)

            select_query = """SELECT * FROM institutes WHERE id = ?"""
            items_tuple = (i_id,)

            cursor_content = self.__db_handler.execute_query(
                select_query, items=items_tuple
            )

            for row in cursor_content:
                inst = Institute(*row)

            cls()
            print("Вы хотите изменить информацию о институте:")
            inst.show()

            print("Доступные действия:")
            print("1. Редактировать название института")
            print("2. Выбрать директора института")

            action = int(input())
            cls()

            if action == 1:
                inst_copy = inst
                print("Введите полное название института")
                f_name = input()
                inst_copy._full_name = f_name

                print("Введите краткое название института")
                sh_name = input()
                inst_copy._short_name = sh_name

                cls()
                print("Вы хотите внести изменения:")
                inst_copy.show()

                print("\nПодтвердите действие [д/Н]")
                if input() == 'д':
                    update_query = """
                    UPDATE institutes
                    SET full_name = ?
                    SET short_name = ? 
                    WHERE id = ?"""

                    items_tuple = (f_name, sh_name, i_id)

                    self.__db_handler.execute_query(
                        update_query, items=items_tuple, commit=True
                    )

            elif action == 2:
                select_query = """
                SELECT teachers.id, teachers.first_name, teachers.second_name, teachers.last_name, teachers.phone_number, institutes.full_name
                FROM teachers JOIN institutes
                ON teachers.institute_id = institutes.id
                WHERE institute_id = ?
                """
                items_tuple = (i_id,)
                cursor_content = self.__db_handler.execute_query(
                    select_query, items=items_tuple
                )

                teachers_available = []
                for row in cursor_content:
                    teachers_available.append(Teacher(*row))

                cls()
                print("Доступные преподаватели для текущего института:\n")
                for teacher in teachers_available:
                    teacher.show()
                    print()

                print("Введите ID нового директора института:")
                h_id = int(input())

                update_query = """
                    UPDATE institutes
                    SET head_id = ? 
                    WHERE id = ?"""

                items_tuple = (h_id, i_id)
                self.__db_handler.execute_query(
                    update_query, items=items_tuple, commit=True
                )
            else:
                print("Некорректный ввод")
                return

        except ValueError as _ex:
            cls()
            print('Ошибка:', _ex, sep=' ')
            return
        except Exception:
            print("Что то не так")
        else:
            print("Запись об институте успешно изменена")
            return
