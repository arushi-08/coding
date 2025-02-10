class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance

    def is_valid_account(self, account: int):
        return 0 <= account <= self.n
    
    def has_balance(self, account: int, money: int):
        return self.balance[account-1] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            self.is_valid_account(account1) and 
            self.is_valid_account(account2) and 
            self.has_balance(account1, money)
            ):
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.is_valid_account(account):
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.is_valid_account(account) and self.has_balance(account, money):
            self.balance[account-1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
