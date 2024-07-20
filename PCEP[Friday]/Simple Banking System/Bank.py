from Account import *
class Bank:
    def __init__(self, name:str) -> None:
        self.name = name
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_number:str, account_holder:str) -> bool:
        if account_number not in self.accounts:
            account = Account(account_number,account_holder)
            self.accounts[account_number] = account
            return True
        else:
            return False
    
    def get_account(self, account_number:str) -> Account | None:
        return self.accounts.get(account_number, None)
    
    def deposit(self,account_number:str, amount:float)-> bool:
        account = self.get_account(account_number)
        if account:
            return account.deposit(amount)
        else:
            False

    def withdraw(self, account_number:str, amount:float)-> bool:
        account = self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        else:
            return False
    def display_account_details(self, account_number:str) -> str:
        account = self.get_account(account_number)
        if account:
            return account.get_details()
        else:
            return "Account Not Found!"
    def __str__(self)-> str:
        return f"{self.name} Bank with {len(self.accounts)} accounts"
    