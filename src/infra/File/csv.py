import csv
from src.domain.Twitter.TweetList import TweetList


class Csv:
    def __init__(self, file_path: str, file_name: str) -> None:
        self.file_path = file_path
        self.file_name = file_name

    def create(self, data: TweetList) -> None:
        with open(self.file_path + self.file_name, 'w', newline='') as f:
            writer = csv.writer(f, lineterminator='\n')
            for row in data.get():
                writer.writerow(row)
            f.close()
