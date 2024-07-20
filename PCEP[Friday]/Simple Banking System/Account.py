class Account:
    def __init__(self, account_number:int, account_holder) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    
    def deposit(self,amount) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount:float) -> bool:
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
    
    def get_details(self) -> str:
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance:.2f}"
    
    def __str__(self) -> str:
        return f"Account({self.account_number}, {self.account_holder}, {self.balance:.2f})"
    
if __name__ == "__main__":
    mrE = Account(12345, "Estevan Anguiano")
    print(mrE.get_details())
    mrE.deposit(100)
    print(mrE.__str__())
    mrE.withdraw(50)
    print(mrE.get_details())