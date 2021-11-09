from src.infra.Database.MySqlConnector import MySqlConnector


class Query(MySqlConnector):
    def __init__(self) -> None:
        MySqlConnector.__init__(self)
        self.cnx = self.get_connector()
        self.cur = self.cnx.cursor()

    def __get_value(self, values: list) -> str:
        return '({parameters})'.format(
            parameters=', '.join(str('\'' + str(parameter) + '\'') for parameter in values)
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
        except:
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
        except:
            self.cnx.rollback()
            self.cnx.close()
            return False
