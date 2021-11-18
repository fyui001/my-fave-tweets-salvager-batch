from src.domain.Common.StringValue import StringValue


class MediaType(StringValue):
    def __init__(self, value: str) -> None:
        StringValue.__init__(self, value)
