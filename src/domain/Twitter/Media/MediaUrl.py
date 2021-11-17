from src.domain.Common.UrlValue import UrlValue


class MediaUrl(UrlValue):
    def __init__(self, value: str):
        UrlValue.__init__(self, value)
