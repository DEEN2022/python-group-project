

# GROUP MEMBERS FOR PYTHON FINAL PROJECT
# 1. MUSIIMIRE EMILY REG-NO: M22B13/015 ACCESS-NO: A98252
# 2. SANTINO JOHN REG-NO: J22B13/055 ACCESS-NO: A97002
# 3. MAGEZI MOSES TIMOTHY REG-NO: S22B13/016 ACCESS-NO: A98726

from datetime import datetime

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.accounts = []

    def create_account(self, account_type, balance):
        account = BankAccount(account_type, balance)
        self.accounts.append(account)
        return account

class BankAccount:
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
        else:
            raise ValueError("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

class Transaction:
    def __init__(self, sender, receiver, amount, description):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()

user1 = User(1, "user1", "password123")
user2 = User(2, "user2", "securepass")

checking_account_user1 = user1.create_account("Checking", 1000)

savings_account_user2 = user2.create_account("Savings", 5000)

checking_account_user1.deposit(500)
checking_account_user1.withdraw(200)

savings_account_user2.deposit(1000)
savings_account_user2.withdraw(200)

print(f"{user1.username}'s Checking Account Balance: ${checking_account_user1.get_balance()}")
print(f"{user2.username}'s Savings Account Balance: ${savings_account_user2.get_balance()}")

print(f"{user1.username}'s Checking Account Transactions: {checking_account_user1.get_transactions()}")
print(f"{user2.username}'s Savings Account Transactions: {savings_account_user2.get_transactions()}")


