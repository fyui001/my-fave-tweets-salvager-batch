from src.app.Services.TakadaYukiServicee import TakadaYukiService
from src.domain.Twitter.AccountName import AccountName


class TakadaYukiPresentation():
    def __init__(self, account_name: AccountName):
        self.service = TakadaYukiService(account_name)

    def save_all_tweets(self, save_format: str) -> None:
        self.service.save_all_tweets(save_format)
