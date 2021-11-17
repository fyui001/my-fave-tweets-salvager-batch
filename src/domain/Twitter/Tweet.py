from src.domain.Twitter.Account import Account
from src.domain.Twitter.TweetId import TweetId
from src.domain.Twitter.TweetUrl import TweetUrl


class Tweet:
    def __init__(self, account: Account, tweet_id: TweetId, content: str, source: str, tweet_url: TweetUrl) -> None:
        self.__tweet_id: TweetId = tweet_id
        self.__account: Account = account
        self.__tweet_url = tweet_url
        self.__content = content
        self.__source = source

    def get_tweet_id(self) -> TweetId:
        return self.__tweet_id

    def get_account(self) -> Account:
        return self.__account

    def get_tweet_url(self) -> TweetUrl:
        return self.__tweet_url

    def get_content(self) -> str:
        return self.__content

    def get_source(self) -> str:
        return self.__source
