import classes
import db_handler as db


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

        if 'department_heads' or 'hr_employees' in self.__user_roles:
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
        pass

    def __get_group_ID(self, group_name):
        pass

    def get_all_groups(self):
        print('Введите название каферды (полное или краткое)')
        dep_name = input()
        dep_id = self.__get_department_ID(dep_name)
        select_query = f"""SELECT * FROM Groups WHERE department_id = {dep_id}"""

        pass

    def get_all_students(self, group_name):
        pass

    def get_all_teachers(self, department_name):
        pass

    def get_personal_info(self):
        pass

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
