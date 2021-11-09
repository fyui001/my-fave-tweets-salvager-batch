from src.domain.Twitter.Account import Account
from src.domain.Twitter.TweetId import TweetId
from src.domain.Twitter.TweetUrl import TweetUrl


class Tweet:
    def __init__(self, account: Account, tweet_id: TweetId) -> None:
        self.__tweet_id: TweetId = tweet_id
        self.__account: Account = account
        self.tweet_url = TweetUrl(
            self.__account.get_account_name(),
            self.__tweet_id,
        )
