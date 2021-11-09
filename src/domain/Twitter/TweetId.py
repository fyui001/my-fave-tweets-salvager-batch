from src.domain.Common.PositiveIntegerValue import PositiveIntegerValue


class TweetId(PositiveIntegerValue):
    def __init__(self, value: int) -> None:
        PositiveIntegerValue.__init__(self, value)
