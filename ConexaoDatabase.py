import psycopg2
import pandas as pd

class ConexaoDatabase():
    def __init__(self, *, host, database, user, password, port):
        self._db_host = host
        self._db_name = database
        self._db_user = user
        self._db_password = password
        self._db_port = port

    def connect_to_database(self):
        try:
            conexao = psycopg2.connect(
                database = self._db_name,
                port = self._db_port,
                user = self._db_user,
                password = self._db_password,
                host = self._db_host)
            
            print(conexao.info)
            return conexao
        except Exception as e:
            raise NameError(f'Error conneting to database {e}')
    

    def select_databse(self, query):
        conexao = self.connect_to_database()
        cursor = conexao.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            raise NameError(f'Falha na consulta: {e}')



    @property
    def db_host(self):
        return self._db_host
    @db_host.setter
    def db_host(self, value):
        self._db_host = value

    @property
    def db_name(self):
        return self._db_name
    @db_name.setter
    def db_name(self, value):
        self._db_name = value

    @property
    def db_user(self):
        return self._db_user
    @db_user.setter
    def db_user(self, value):
        self._db_user = value

    @property
    def db_password(self):
        return self._db_password
    @db_password.setter
    def db_password(self, value):
        self._db_password = value

    @property
    def db_port(self):
        return self._db_port
    @db_port.setter
    def db_port(self, value):
        self._db_port = value

if __name__ == '__main__':
    teste = ConexaoDatabase(
        database='bohr_estagiarios_2',
        host='10.100.64.55',
        port='5432',
        user='postgres',
        password='dpmg2022')
    
    consulta = 'select * from tb_auxiliar_gabriel'

    conexao = teste.connect_to_database()

    data = pd.read_sql_query(consulta, con=conexao)

    print(data.head())
    print(data.tail())
    print(data.columns)

