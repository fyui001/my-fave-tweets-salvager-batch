from src.domain.Twitter.TweetList import TweetList
from src.domain.Twitter.Media.MediaList import MediaList
from src.domain.Twitter.Account.AccountName import AccountName
from src.domain.Models.MyFave import MyFave
from src.domain.Models.MyFaveTweet import MyFaveTweet
from src.domain.Models.MediaUrl import MediaUrl
from src.app.Services.GetAllTweetsService import GetAllTweetsService
from src.app.Services.BaseService import BaseService


class TakadaYukiService(BaseService):
    def __init__(self, account_name: AccountName) -> None:
        BaseService.__init__(self)
        self.__account_name = account_name
        self.__fave_name = '高田憂希'
        self.__my_fave_id: int = 0
        self.__import_data: dict = {}
        self.__tweet_list: TweetList = TweetList([])
        self.__media_list: MediaList = MediaList([])

    async def save_all_tweets(self, save_format: str) -> None:
        get_all_tweets_service = GetAllTweetsService(self.__account_name)
        result: dict = await get_all_tweets_service.get_all_tweets()
        self.__tweet_list = result['tweet_list']
        self.__media_list = result['media_list']
        my_fave = MyFave().get_my_fave_id(self.__fave_name)
        for key in my_fave:
            self.__my_fave_id = int(key['id'])
        for arr in self.__tweet_list.get_value():
            arr.insert(0, self.__my_fave_id)
        tweet_import_data: list = self.__tweet_list.get_value()
        media_import_data: list = self.__media_list.get_value()
        if save_format == 'db':
            MyFaveTweet().save_all_tweets(tweet_import_data)
            #MediaUrl().save_media_urls(media_import_data)
        elif save_format == 'csv':
            self.gen_csv(self.__tweet_list, self.__account_name)

