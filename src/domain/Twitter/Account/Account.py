from src.domain.Twitter.Account.AccountName import AccountName


class Account:
    def __init__(self, value: AccountName):
        self.__account_name = value

    def get_account_name(self) -> AccountName:
        return self.__account_name
