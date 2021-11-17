from src.infra.Database.Query import Query


class MyFaveTweet:
    def __init__(self) -> None:
        self.__table = 'my_fave_tweets'
        self.__columns = [
            'fave_id',
            'account_name',
            'tweet_id',
            'tweet_url',
            'content',
            'tweet_source',
        ]

    def save_all_tweets(self, data: list):
        Query().bulk_insert(self.__table, self.__columns, data)
