import os
from classes import *
import db_handler as db


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class db_client(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__db_handler = db.database_handler()
        self.__connection = self.__db_handler.connect(self.username, self.password)
        self.__user_roles = self.__get_user_roles()

    def __del__(self):
        self.__db_handler.close_connection()

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

        if 'department_heads' in self.__user_roles \
            or 'hr_employees' in self.__user_roles:
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
                self.add_department_head,
                self.del_department_head,
                self.edit_department_info,
            ):
                user_actions[it] = function
                it += 1
        
        return user_actions

    def __get_department_ID(self, department_name):
        try:
            select_query = """SELECT id FROM departments WHERE short_name = ?"""
            items_tuple = (department_name, )
            cursor_content = self.__db_handler.execute_query(select_query, items=items_tuple)
            return list(cursor_content)[0][0]
        except Exception:
            return -1

    def __get_group_ID(self, group_name):
        try:
            select_query = """SELECT id FROM groups WHERE short_name = ? """
            items_tuple = (group_name, )
            cursor_content = self.__db_handler.execute_query(select_query, items=items_tuple)
    
            return list(cursor_content)[0][0]
        except Exception:
            return -1

    def get_all_groups(self):
        print('Введите название института (краткое)')
        dep_name = input()
        dep_id = self.__get_department_ID(dep_name)

        if dep_id == -1:
            print('Такого института не существует')
            return

        select_query = """
        SELECT groups.id, groups.full_name, groups.short_name, groups.student_count, departments.full_name 
        FROM groups JOIN departments
        ON department_id = departments.id
        WHERE department_id = ?
        """

        items_tuple = (dep_id, )
        cursor_content = self.__db_handler.execute_query(select_query, items=items_tuple)

        group_list = []
        for row in cursor_content:
            group_list.append(Group(*row))

        cls()
        for group in group_list:
            group.show()
            print()

    def get_all_students(self):
        print('Введите название каферды (краткое)')
        group_name = input()
        group_id = self.__get_group_ID(group_name)

        if group_id == -1:
            print("Такой группы не существует")
            return

        select_query = """
        SELECT gradebook_number, first_name, second_name, last_name, phone_number, birth_date, full_name
        FROM students JOIN groups 
        ON group_id = id
        WHERE group_id = ?"""

        items_tuple = (group_id, )

        cursor_content = self.__db_handler.execute_query(select_query, items=items_tuple)
        students_list = []

        for row in cursor_content:
            students_list.append(Student(*row))

        cls()
        for student in students_list:
            student.show()
            print()


    def get_all_teachers(self):
        print("Введите название института (краткое)")
        dep_name = input()
        dep_id = self.__get_department_ID(dep_name)

        if dep_id == -1:
            print("Такого института не существует")
            return

        select_query = """
        SELECT teachers.id, teachers.first_name, teachers.second_name, teachers.last_name, teachers.phone_number, departments.full_name
        FROM teachers JOIN departments
        ON teachers.department_id = departments.id
        WHERE department_id = ?"""

        items_tuple = (dep_id, )
        cursor_content = self.__db_handler.execute_query(select_query, items=items_tuple)
        teachers_list = []
        for row in cursor_content:
            teachers_list.append(Teacher(*row))

        cls()
        for teacher in teachers_list:
            teacher.show()
            print()

    def get_personal_info(self):
        print("Введите свой ID:")
        teacher_id = int(input())

        select_query = """
        SELECT teachers.id, teachers.first_name, teachers.second_name, teachers.last_name, teachers.phone_number, departments.full_name
        FROM teachers JOIN departments
        ON teachers.department_id = departments.id
        WHERE teachers.id = ?"""

        items_tuple = (teacher_id, )
        cursor_content = self.__db_handler.execute_query(select_query, items=items_tuple)

        teacher_info = None
        for row in cursor_content:
            teacher_info = Teacher(*row)

        teacher_info.show()
        print()

    def add_student(self):
        pass

    def del_student(self):
        pass

    def add_teacher(self):
        pass

    def del_teacher(self):
        pass

    def add_department_head(self):
        pass

    def del_department_head(self):
        pass

    def edit_department_info(self):
        pass
