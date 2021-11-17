from src.domain.Common.ListValue import ListValue
from src.domain.Twitter.Tweet import Tweet


class TweetList(ListValue):
    def __init__(self, value: list) -> None:
        ListValue.__init__(self, value)
