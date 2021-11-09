from src.domain.Common.StringValue import StringValue


class AccountName(StringValue):
    def __init__(self, value: str) -> None:
        StringValue.__init__(self, value)
