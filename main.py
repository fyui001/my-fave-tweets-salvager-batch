import argparse
import logging
import os
from src.DbConnector import DbConnector
from src.CsvGenerator import CsvGenerator
from dotenv import load_dotenv
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened

class GetFaveTweets:

    def __init__(self, fave_name):
        self.fave_name = fave_name
        self.tweet_url = 'https://twitter.com/{fave_name}/status/{tweet_id}'
        self.result = {}
        self.import_data = []

    def __get_fave_tweets(self, user_name: str) -> None:

        # twitterクライアントの設定
        tw_client = Twarc2(
            consumer_key=os.getenv("CONSUMER_KEY"),
            consumer_secret=os.getenv("CONSUMER_SECRET")
        )

        # queryの設定をしてツイートを1件ずつ取得する
        query = 'from:{user_name}'.format(user_name = user_name)

        for page in tw_client.search_all(query=query):
            for tweet in ensure_flattened(page):
                self.result[tweet.get('id')] = tweet.get('created_at')

        self.result = sorted(self.result.items(), key=lambda x:x[1])

    def __data_processor(self):
        self.import_data = []
        # データ整形
        for k in self.result:
            self.import_data.append([
                self.fave_name,
                k[0],
                self.tweet_url.format(fave_name=self.fave_name, tweet_id=k[0])
            ])

    def import_database(self) -> None:
        self.__get_fave_tweets(self.fave_name)

        table = 'my_fave_tweets_sample'
        columns = [
            'account_name',
            'tweet_id',
            'tweet_url',
        ]
        self.__data_processor()
        db_client = DbConnector()
        db_client.bulk_insert(table, columns, self.import_data)

    def generate_csv(self) -> None:
        self.__get_fave_tweets(self.fave_name)
        self.__data_processor()

        csv_generator = CsvGenerator()
        csv_generator.gen_csv(self.import_data, self.fave_name)

def main():

    # dotenvの読み込み
    base_path = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(base_path, '.env')
    load_dotenv(dotenv_path)

    # ログの設定
    logger = logging.getLogger("get-tweets")
    logging.basicConfig(level=logging.INFO)

    # コマンドライン引数の設定と取得
    parser = argparse.ArgumentParser(
        'get all tweet', usage='python main.py --user-id=sunflower930316 --save-format=db|csv'
    )

    # ユーザーIDを取得する引数設定
    parser.add_argument(
        '--user-id',
        help='取得したいツイッターアカウントのユーザーIDを指定する。高田憂希のツイートを取得した場合は[sunflower930316]',
        type=str,
        required=True,
    )

    # 保存するフォーマットを指定する引数の指定
    parser.add_argument(
        '--save-format',
        help='保存するフォーマットを指定する。データベースに保存したい場合は[db]、CSV形式でファイル出力したい場合は[csv]',
        type=str,
        required=True,
    )

    args = parser.parse_args()
    user_id = args.user_id
    save_format = args.save_format

    getter = GetFaveTweets(user_id)

    if save_format == 'db':
        getter.import_database()
    elif save_format == 'csv':
        getter.generate_csv()

    logger.info('取得完了しました')
    print('高田憂希しか好きじゃない')

if __name__ == '__main__':
    main()