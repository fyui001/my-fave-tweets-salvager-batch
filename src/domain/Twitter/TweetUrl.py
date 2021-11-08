from src.domain.Twitter.AccountName import AccountName
from src.domain.Twitter.TweetId import TweetId


class TweetUrl:
    def __init__(self) -> None:
        self.__tweet_url_tmp: str = 'https://twitter.com/{account_name}/status/{tweet_id}'

    def get_tweet_url(self, account_name: AccountName, tweet_id: TweetId) -> str:
        return self.__tweet_url_tmp.format(
            account_name=account_name,
            tweet_id=tweet_id
        )
