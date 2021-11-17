from src.infra.Database.Query import Query


class MyFave:
    def __init__(self) -> None:
        self.__table = 'my_faves'
        self.__columns = [
            'name',
        ]

    def get_my_fave_id(self, name: str):
        select_columns = [
            'id',
        ]
        where = {
            'name': name
        }
        return Query().select(self.__table, select_columns, where)

