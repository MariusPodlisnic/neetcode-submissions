class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self,name: str,balance: int) -> None:
        self.name = name
        self.balance = balance

    def increase_total_accounts(self) -> None:
        BankAccount.total_accounts += 1
    
    def increase_total_balance(self) -> None:
        BankAccount.total_balance += self.balance

# TODO: Create two accounts
first_account = BankAccount("Alice",1000)
first_account.increase_total_accounts()
first_account.increase_total_balance()
second_account = BankAccount("Bob",2000)
second_account.increase_total_accounts()
second_account.increase_total_balance()
# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${first_account.balance}")
print(f"Bob's balance: ${second_account.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")