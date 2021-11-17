from src.domain.Twitter.TweetId import TweetId
from src.domain.Twitter.Media.MediaKey import MediaKey
from src.domain.Twitter.Media.MediaUrl import MediaUrl
from src.domain.Twitter.Media.MediaType import MediaType


class Media:
    def __init__(self, tweet_id: TweetId, media_key: MediaKey, media_url: MediaUrl, media_type: MediaType):
        self.__tweet_id = tweet_id
        self.__media_key = media_key
        self.__media_url = media_url
        self.__media_type = media_type

    def get_tweet_id(self) -> TweetId:
        return self.__tweet_id

    def get_media_key(self) -> MediaKey:
        return self.__media_key

    def get_media_url(self) -> MediaUrl:
        return self.__media_url

    def get_media_type(self) -> MediaType:
        return self.__media_type
