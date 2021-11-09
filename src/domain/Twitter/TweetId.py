from src.domain.Common.PositiveIntegerValue import PositiveIntegerValue


class TweetId(PositiveIntegerValue):
    def __init__(self, value: str) -> None:
        PositiveIntegerValue.__init__(self, value)
