from src.infra.Database.Query import Query


class MediaUrl:
    def __init__(self) -> None:
        self.__table = 'media_urls'
        self.__columns = [
            'tweet_id',
            'media_key',
            'url',
            'type',
        ]

    def save_media_urls(self, data) -> None:
        Query().bulk_insert(self.__table, self.__columns, data)
