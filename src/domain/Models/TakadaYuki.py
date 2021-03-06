from src.infra.Database.Query import Query
from src.domain.Twitter.TweetList import TweetList


class TakadaYuki:
    def __init__(self) -> None:
        self.__table = 'takada_yuki_tweets'
        self.__columns = [
            'account_name',
            'tweet_id',
            'tweet_url',
            'content',
            'tweet_source',
        ]

    def save_all_tweets(self, tweets: TweetList):
        Query().bulk_insert(self.__table, self.__columns, tweets.get_value())
