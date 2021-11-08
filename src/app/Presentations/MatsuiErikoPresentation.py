from src.app.Services.MatsuiErikoService import MatsuiErikoService
from src.domain.Twitter.AccountName import AccountName


class MatsuiErikoPresentation():
    def __init__(self, account_name: AccountName):
        self.service = MatsuiErikoService(account_name)

    def save_all_tweets(self, save_format: str) -> None:
        self.service.save_all_tweets(save_format)
