import mysql.connector as connector
import os


class DbConnector:

    def __db_connect(self) -> None:
        try:
            db = connector.connect(
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWD'),
                host=os.getenv('DB_HOST'),
                db=os.getenv('DB_DATABASE'),
                auth_plugin="mysql_native_password"
            )
            return db
        except Exception as e:
            print(e)
            raise

    def __get_value(self, values: list) -> str:
        return '({parameters})'.format(
            parameters=', '.join(str('\'' + str(parameter) + '\'') for parameter in values)
        )

    def insert(self, table: str, values: dict) -> bool:
        cnx = self.__db_connect()
        cur = cnx.cursor()

        columns = list(values.keys())
        parameters = list(values.values())

        sql = "INSERT INTO `{table}` ({columns}) VALUES ({values})".format(
            table=table,
            columns=', '.join(columns),
            values=', '.join(str('\'' + parameter + '\'') for parameter in parameters)
        )

        try:
            cur.execute(sql)
            cnx.commit()
            return True
        except:
            cnx.rollback()
            return False

    def bulk_insert(self, table: str, columns: list, values: list) -> bool:
        cnx = self.__db_connect()
        cur = cnx.cursor()
        parameters = []
        for value in values:
            parameters.append(self.__get_value(value))

        sql = "INSERT INTO `{table}` ({columns}) VALUES {values}".format(
            table=table,
            columns=', '.join(columns),
            values=', '.join(parameters)
        )

        try:
            cur.execute(sql)
            cnx.commit()
            return True
        except:
            cnx.rollback()
            return False

    def select(self, sql: str) -> list:
        cnx = self.__db_connect()
        cur = cnx.cursor(dictionary=True)
        try:
            cur.execute(sql)
            response = cur.fetchall()
            cur.close()
        except:
            return []

        return response