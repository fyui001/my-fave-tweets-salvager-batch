from src.infra.Database.Query import Query
from src.domain.Twitter.TweetList import TweetList


class MatsuiEriko:
    def __init__(self):
        self.__table = 'matsui_eriko_tweets'
        self.__columns = [
            'account_name',
            'tweet_id',
            'tweet_url',
        ]

    def save_all_tweets(self, tweets: TweetList):
        Query().bulk_insert(self.__table, self.__columns, tweets.get())
