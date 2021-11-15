import pyodbc as db


class database_handler(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(database_handler, cls).__new__(cls)
        return cls.instance
    
    def connect(self, username, password):
        try:
            self.connection = db.connect(
                f"""DSN=MSSQLServerDatabase;
                    DATABASE=university;
                    UID={username};
                    PWD={password}"""
            )
            self.cursor = self.connection.cursor()
            print(f'Connected as {username}')
        except Exception as _ex:
            print('Connection failure', _ex, sep='\n')
            return -1

    def close_connection(self):
        try:
            self.cursor.close()
            self.connection.close()
            print('Connection closed')
        except Exception as _ex:
            print('Close connection failure', _ex, sep='\n')

    def execute_query(self, query, items=None, commit=False):
        try:
            if items is None:
                self.cursor.execute(query)
            else:
                if commit:
                    self.cursor.execute(query, items)
                    self.cursor.commit()
                else:
                    self.cursor.execute(query, items)

        except Exception as _ex:
            print('Execution failure', _ex, sep='\n')
        else:
            return self.cursor
