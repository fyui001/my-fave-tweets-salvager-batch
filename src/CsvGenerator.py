import csv
import os
from datetime import datetime, timedelta, timezone
import logging
import sys

class CsvGenerator:
    def __init__(self):
        self.file_path = sys.path[0] + '/output/{time}-{user_name}/'
        self.file_name = '{user_name}.csv'
        self.JST = timezone(timedelta(hours=+9), 'JST')

    def gen_csv(self, tweets_data: list, user_name: str) -> bool:

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("gen-csv")

        now = datetime.strptime(datetime.now(self.JST).strftime("%Y-%m-%d %H:%M:%S.%f"), '%Y-%m-%d %H:%M:%S.%f')

        self.file_path = self.file_path.format(
            time = now,
            user_name = user_name
        )

        self.file_name = self.file_name.format(
            user_name = user_name
        )

        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)
        else:
            logger.error('ディレクトリはすでに存在します')
            return False

        with open(self.file_path + self.file_name, 'w', newline='') as f:
            writer = csv.writer(f, lineterminator='\n',)
            for row in tweets_data:
                writer.writerow(row)
            f.close()

        logger.info('出力完了: ' + self.file_path + self.file_name)

        return True