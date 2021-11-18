class ListValue:
    def __init__(self, value: list):
        self.__value: list = value

    def get_value(self) -> list:
        return self.__value

    def append(self, value: list) -> None:
        self.__value.append(value)
