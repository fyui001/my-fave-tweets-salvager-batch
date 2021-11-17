from src.infra.Database.MySqlConnector import MySqlConnector


class Query(MySqlConnector):
    def __init__(self) -> None:
        MySqlConnector.__init__(self)
        self.cnx = self.get_connector()
        self.cur = self.cnx.cursor()

    def __get_value(self, values: list) -> str:
        return '({parameters})'.format(
            parameters=', '.join(repr(parameter) for parameter in values)
        )

    def insert(self, table: str, values: dict) -> bool:

        columns = list(values.keys())
        parameters = list(values.values())

        sql = "INSERT INTO `{table}` ({columns}) VALUES ({values})".format(
            table=table,
            columns=', '.join(columns),
            values=', '.join(str('\'' + parameter + '\'') for parameter in parameters)
        )

        try:
            self.cur.execute(sql)
            self.cnx.commit()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            self.cnx.rollback()
            self.cnx.close()
            return False

    def bulk_insert(self, table: str, columns: list, values: list) -> bool:
        parameters = []
        for value in values:
            parameters.append(self.__get_value(value))
        sql = "INSERT INTO `{table}` ({columns}) VALUES {values}".format(
            table=table,
            columns=', '.join(columns),
            values=', '.join(parameters)
        )
        try:
            self.cur.execute(sql)
            self.cnx.commit()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            self.cnx.rollback()
            self.cnx.close()
            return False

    def select(self, table: str, columns: list = [], where: dict = {}):
        cur = self.cnx.cursor(dictionary=True)
        sql = ''

        if len(columns) == 0 and len(where) == 0:
            sql = "SELECT * FROM `{table}`".format(
                table=table,
            )
        elif len(columns) != 0 and len(where) == 0:
            sql = "SELECT {columns} FROM {table}".format(
                columns=', '.join(columns),
                table=table
            )
        elif len(columns) == 0 and len(where) != 0:
            where_column = where.keys()
            where_value = where.values()

            sql = "SELECT * FROM `{table}` WHERE {where_column} = {where_value}".format(
                table=table,
                where_column=''.join(column for column in where_column),
                where_value=''.join(str('\'' + str(value) + '\'') for value in where_value)
            )
            try:
                cur.execute(sql)
                response = cur.fetchall()
                cur.close()
                return response
            except Exception as e:
                print(e)
                return False

        elif len(columns) != 0 and len(where) != 0:
            where_column = where.keys()
            where_value = where.values()

            sql = "SELECT {select_column} FROM `{table}` WHERE {where_column} = {where_value}".format(
                table=table,
                select_column=', '.join(columns),
                where_column=''.join(column for column in where_column),
                where_value=''.join(str('\'' + str(value) + '\'') for value in where_value)
            )
            try:
                cur.execute(sql)
                response = cur.fetchall()
                cur.close()
                return response
            except Exception as e:
                print(e)
                print(cur.statement)
                return False
        try:
            cur.execute(sql)
            response = cur.fetchall()
            cur.close()
            return response
        except Exception as e:
            print(e)
            return False

