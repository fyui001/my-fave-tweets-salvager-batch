import os
from datetime import datetime, timedelta, timezone
import logging
import sys
from src.infra.File.csv import Csv
from src.domain.Twitter.TweetList import TweetList
from src.domain.Twitter.Account.AccountName import AccountName


class BaseService:
    def __init__(self) -> None:
        self.file_path = sys.path[0] + '/output/{time}-{user_name}/'
        self.file_name = '{user_name}.csv'
        self.JST = timezone(timedelta(hours=+9), 'JST')

    def gen_csv(self, data: TweetList, account_name: AccountName) -> bool:

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("gen-csv")

        now = datetime.strptime(datetime.now(self.JST).strftime("%Y-%m-%d %H:%M:%S.%f"), '%Y-%m-%d %H:%M:%S.%f')

        self.file_path = self.file_path.format(
            time=now,
            user_name=account_name.get_value()
        )

        self.file_name = self.file_name.format(
            user_name=account_name.get_value()
        )

        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)
        else:
            logger.error('ディレクトリはすでに存在します')
            return False

        try:
            Csv(self.file_path, self.file_name).create(data)
        except:
            return False
