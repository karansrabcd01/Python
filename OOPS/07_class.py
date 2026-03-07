"""
Problem 1: Bank Account System

Create a class BankAccount with:

Attributes:

account_holder

balance

Methods:

deposit(amount)

withdraw(amount)

check_balance()

Conditions:

Cannot withdraw more than balance

Balance should never be negative

Write full code.
"""


class BankAccount:
    def __init__(self, account_holder, balance=0):
        """
        Constructor to initialize account holder name and balance.
        Default Balance is 0 if not provided.
        """
        self.account_holder = account_holder
        self.balance = balance if balance >= 0 else 0

    def deposit(self, amount):
        """
        Deposits money into the account.
        Amount must be positive.
        """
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        Cannot withdraw more than available balance.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")

    def check_balance(self):
        """
        Returns the current balance.
        """
        print(f"Current Balance: Rs. {self.balance}")


if __name__ == "__main__":
    # Create account
    account1 = BankAccount("Abhishek", 1000)

    # Check balance
    account1.check_balance()

    # Deposit money
    account1.deposit(500)

    # Withdraw money
    account1.withdraw(300)

    # Try to withdraw more than balance
    account1.withdraw(2000)

    # Final balance
    account1.check_balance()
