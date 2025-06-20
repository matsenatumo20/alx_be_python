class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.__account_balance = initial_balance

    def deposit(self, amount: float):
        if ammont < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.__account_balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdrawal cannot be negative")
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True
    
    def display_balance(self):
        print(f"Current Balance: {self.__account_balance:.2f}")
