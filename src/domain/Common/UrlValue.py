from urllib.parse import urlparse


class UrlValue:
    def __init__(self, value: str):
        o = urlparse(value)

        if len(o) == 0:
            raise

        self.__value = value

    def get_value(self) -> str:
        return self.__value
