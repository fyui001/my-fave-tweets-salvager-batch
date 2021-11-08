from src.domain.Twitter.AccountName import AccountName
from src.domain.Models.MatsuiEriko import MatsuiEriko
from src.app.Services.GetAllTweetsService import GetAllTweetsService
from src.app.Services.BaseService import BaseService


class MatsuiErikoService(BaseService):
    def __init__(self, account_name: AccountName) -> None:
        BaseService.__init__(self)
        self.__account_name = account_name

    async def save_all_tweets(self, save_format: str) -> None:
        get_all_tweets_service = GetAllTweetsService(self.__account_name)
        tweet_list = await get_all_tweets_service.get_all_tweets()
        if save_format == 'db':
            MatsuiEriko().save_all_tweets(tweet_list)
        elif save_format == 'csv':
            self.gen_csv(tweet_list, self.__account_name)

