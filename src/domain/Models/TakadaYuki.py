from src.infra.Database.Query import Query
from src.domain.Twitter.TweetList import TweetList
from src.domain.Twitter.Account import Account


class TakadaYuki:
    def __init__(self):
        self.__table = 'takada_yuki_tweets'
        self.__columns = [
            'account_name',
            'tweet_id',
            'tweet_url',
        ]

    def save_all_tweets(self, tweets: TweetList):
        Query().bulk_insert(self.__table, self.__columns, tweets.get_value())
