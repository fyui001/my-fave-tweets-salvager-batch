from src.domain.Common.UrlValue import UrlValue
from src.domain.Twitter.Account.AccountName import AccountName
from src.domain.Twitter.TweetId import TweetId


class TweetUrl(UrlValue):
    def __init__(self, account_name: AccountName, tweet_id: TweetId) -> None:
        self.__tweet_url_tmp: str = 'https://twitter.com/{account_name}/status/{tweet_id}'
        self.__tweet_url = self.__tweet_url_tmp.format(
            account_name=account_name.get_value(),
            tweet_id=tweet_id.get_value()
        )
        UrlValue.__init__(self, self.__tweet_url)

