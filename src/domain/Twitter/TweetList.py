from src.domain.Common.ListValue import ListValue


class TweetList(ListValue):
    def __init__(self, value: list) -> None:
        ListValue.__init__(self, value)

    def get(self) -> list:
        return self.get_value()

