import mysql.connector as connector
import os


class MySqlConnector:
    def __init__(self) -> None:
        try:
            self.db = connector.connect(
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWD'),
                host=os.getenv('DB_HOST'),
                db=os.getenv('DB_DATABASE'),
                auth_plugin="mysql_native_password"
            )
        except Exception as e:
            print(e)
            raise

    def get_connector(self) -> connector:
        return self.db
