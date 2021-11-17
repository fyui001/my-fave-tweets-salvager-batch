import argparse
import logging
import os
import asyncio
from dotenv import load_dotenv
from src.app.Services.TakadaYukiServicee import TakadaYukiService
from src.app.Services.MatsuiErikoService import MatsuiErikoService
from src.domain.Twitter.Account.AccountName import AccountName


async def main():
    # dotenvの読み込み
    base_path = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(base_path, '.env')
    load_dotenv(dotenv_path)

    # ログの設定
    logger = logging.getLogger("get-tweets")
    logging.basicConfig(level=logging.INFO)

    # コマンドライン引数の設定と取得
    parser = argparse.ArgumentParser(
        'get all tweet', usage='python main.py --account-name=sunflower930316 --save-format=db|csv'
    )

    # ユーザーIDを取得する引数設定
    parser.add_argument(
        '--account-name',
        help='取得したいツイッターアカウントのユーザー名を指定する。高田憂希のツイートを取得した場合は[sunflower930316]',
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
    account_name = AccountName(args.account_name)
    save_format = args.save_format

    if account_name.equal('sunflower930316'):
        await TakadaYukiService(account_name).save_all_tweets(save_format)
        logger.info('高田憂希しか好きじゃない')
    elif account_name.equal('ErikoMatsui'):
        await MatsuiErikoService(account_name).save_all_tweets(save_format)
        logger.info('松井恵理子しか好きじゃない')

    logger.info('取得完了しました')


if __name__ == '__main__' :
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
