from src.domain.Common.ListValue import ListValue


class MediaList(ListValue):
    def __init__(self, value: list) -> None:
        ListValue.__init__(self, value)
