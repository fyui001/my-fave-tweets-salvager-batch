import os
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened
from src.domain.Twitter.Account.AccountName import AccountName
from src.domain.Twitter.Account.Account import Account
from src.domain.Twitter.TweetId import TweetId
from src.domain.Twitter.TweetUrl import TweetUrl
from src.domain.Twitter.TweetList import TweetList
from src.domain.Twitter.Media.Media import Media
from src.domain.Twitter.Media.MediaList import MediaList
from src.domain.Twitter.Media.MediaKey import MediaKey
from src.domain.Twitter.Media.MediaUrl import MediaUrl
from src.domain.Twitter.Media.MediaType import MediaType


class GetAllTweetsService:
    def __init__(self, account_name: AccountName) -> None:
        self.__account_name = account_name
        self.__tweet_list: TweetList = TweetList([])
        self.__tweet_id: int
        self.__tweet_ids: dict = {}
        self.__tweet_texts: dict = {}
        self.__tweet_source: dict = {}
        self.__import_data: dict = {}
        self.__media_lists: MediaList = MediaList([])
        self.__result: dict = {}

    async def __media_builder(self, tweet_id: TweetId, media_key: MediaKey, media_url: MediaUrl, media_type: MediaType) -> None:
        self.__media_lists.append(
            [
                Media(tweet_id, media_key, media_url, media_type)
            ]
        )

    async def __media__dict_builder(self, media: list) -> dict:
        for k in media:
            if k['type'] == 'photo':
                return {
                    'url': k['url'],
                    'type': k['type'],
                }
            elif k['type'] == 'video':
                return {
                    'url': k['preview_image_url'],
                    'type': k['type'],
                }

    async def __media_keys_builer(self, media_keys):
        result = []
        for i in media_keys:
            result.append(i)

        return result

    async def __get_all_tweets(self) -> None:

        # twitterクライアントの設定
        tw_client = Twarc2(
            consumer_key=os.getenv("CONSUMER_KEY"),
            consumer_secret=os.getenv("CONSUMER_SECRET")
        )

        # queryの設定をしてツイートを1件ずつ取得する
        query = 'from:{user_name} -is:retweet'.format(user_name=self.__account_name.get_value())
        for page in tw_client.search_all(query=query):
            for tweet in ensure_flattened(page):
                self.__tweet_id = TweetId(int(tweet.get('id')))
                if tweet.get('attachments'):
                    attachments = [tweet.get('attachments')]
                    for key in attachments:
                        # gifは取れないしいらないのでbreakさせる
                        if 'media'not in key.items():
                            break
                        for media_key in key['media_keys']:
                            media: dict = await self.__media__dict_builder(key['media'])
                            await self.__media_builder(self.__tweet_id, media_key, media['url'], media['type'])
                self.__tweet_ids.update(
                    {
                        self.__tweet_id.get_value(): tweet.get('created_at')
                    }
                )
                self.__tweet_texts.update(
                    {
                        self.__tweet_id.get_value(): tweet.get('text')
                    }
                )
                self.__tweet_source.update(
                    {
                        self.__tweet_id.get_value(): tweet.get('source')
                    }
                )
        for k in sorted(self.__tweet_ids.items(), key=lambda x: x[1]):
            self.__result.update(
                {
                    TweetId(k[0]): self.__tweet_texts[k[0]]
                }
            )

    async def __data_processor(self) -> None:
        # データ整形
        await self.__get_all_tweets()

        for tweet_id, tweet_text in self.__result.items():
            self.__tweet_list.append([
                self.__account_name.get_value(),
                tweet_id.get_value(),
                tweet_text,
                self.__tweet_source[tweet_id.get_value()],
                TweetUrl(self.__account_name, tweet_id).get_value()
            ])
        self.__import_data['tweet_list'] = self.__tweet_list
        self.__import_data['media_list'] = self.__media_lists

    async def get_all_tweets(self) -> dict:
        await self.__data_processor()
        return self.__import_data

