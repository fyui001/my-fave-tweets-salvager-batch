import os
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened
from src.domain.Twitter.AccountName import AccountName
from src.domain.Twitter.TweetId import TweetId
from src.domain.Twitter.TweetUrl import TweetUrl
from src.domain.Twitter.TweetList import TweetList


class GetAllTweetsService:
    def __init__(self, account_name: AccountName) -> None:
        self.__account_name = account_name
        self.__result: dict = {}
        self.__import_data: TweetList = TweetList([])

    async def __get_all_tweets(self) -> None:

        # twitterクライアントの設定
        tw_client = Twarc2(
            consumer_key=os.getenv("CONSUMER_KEY"),
            consumer_secret=os.getenv("CONSUMER_SECRET")
        )

        # queryの設定をしてツイートを1件ずつ取得する
        query = 'from:{user_name}'.format(user_name=self.__account_name.get_value())

        for page in tw_client.search_all(query=query):
            for tweet in ensure_flattened(page):
                self.__result.update(
                    {
                        TweetId(tweet.get('id')).get_value(): tweet.get('created_at')
                    }
                )

        self.__result = sorted(self.__result.items(), key=lambda x: x[1])

    async def __data_processor(self) -> None:
        # データ整形
        await self.__get_all_tweets()

        for key in self.__result:
            self.__import_data.append([
                self.__account_name.get_value(),
                key[0],
                TweetUrl(self.__account_name, key).get_value()
            ])

    async def get_all_tweets(self) -> TweetList:
        await self.__data_processor()
        return self.__import_data
