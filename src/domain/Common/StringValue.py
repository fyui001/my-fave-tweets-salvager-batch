class StringValue:
    def __init__(self, value: str):
        self.__value = value

    def get_value(self) -> str:
        return self.__value

    def equal(self, value: str) -> bool:
        return self.__value == value
