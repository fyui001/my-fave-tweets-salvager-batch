class PositiveIntegerValue:
    def __init__(self, value: int) -> None:
        if value < 0:
            raise

        self.__value = value

    def get_value(self) -> int:
        return self.__value
