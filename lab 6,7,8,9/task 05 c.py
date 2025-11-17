class BankAccount:
    def __init__(self, name, initial_balance=0, account_number=None):
        self.name = name
        self.__balance = initial_balance  # Private attribute
        self.account_number = account_number

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be a positive amount.")
            return
        self.__balance += amount
        print(f"{self.name} deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Withdrawal failed. Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"{self.name} withdrew ${amount}. New balance: ${self.__balance}")

    def check_balance(self):
        print(f"{self.name}'s current balance is: ${self.__balance}")
        return self.__balance

account1 = BankAccount("John Doe", 1000, "1234567890")
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

