from src.domain.Common.StringValue import StringValue


class MediaKey(StringValue):
    def __init__(self, value: str) -> None:
        StringValue.__init__(self, value)