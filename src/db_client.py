import classes
import db_handler as db


class db_client(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__db_handler = db.database_handler()
        self.__connection = self.__db_handler.connect(self.username, self.password)
        self.user_roles = self.__get_user_roles()

    def __get_user_roles(self):
        try:
            roles_query = ""
            roles = self.__db_handler.execute_query(roles_query)
            return roles

        except Exception as _ex:
            print('get_user_roles failure', _ex, sep='\n')


    def __get_department_ID(self, department_name):
        try:
            select_query = "SELECT id FROM departments WHERE full_name = ?"
            dep_id = self.__db_handler.execute_query(select_query, department_name)

            if len(dep_id) == 0:
                print(f'There is no depatment with name: {department_name}')
                return -1
            else:
                return dep_id

        except Exception as _ex:
            print('get_department_ID failure', _ex, sep='\n')


    def __get_group_ID(self, group_name):
        try:
            select_query = "SELECT id FROM groups WHERE full_name = ?"
            group_id = self.__db_handler.execute_query(select_query, group_name)

            if len(group_id) == 0:
                print(f"No group with name {group_name}")
            else:
                return group_id

        except Exception as _ex:
            print('get_groip_ID failure', _ex, sep='\n')


    def get_all_departments(self):
        try:
            select_query = "SELECT * FROM departments"
            departments = self.__db_handler.execute_query(select_query)
            return departments

        except Exception as _ex:
            print('')


    def get_all_students(self, group_name):
        try:
            group_id = self.__get_group_ID(group_name)
            select_query = "SELECT first_name, second_name, last_name FROM students WHERE group_id = ?"
            students = self.__db_handler.execute_query(select_query, group_id)
            return students

        except Exception as _ex:
            print('')


    def get_all_teachers(self, department_name):
        try:
            dep_id = self.__get_department_ID(department_name)
            select_query = "SELECT first_name, second_name, last_name FROM teachers WHERE department_id = ?"
            teachers = self.__db_handler.execute_query(select_query, dep_id)
            return teachers

        except Exception as _ex:
            print('')

    def get_personal_info(self):
        pass
