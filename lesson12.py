class Account:
    def __init__(self, full_name, acc_num, phone, balance):
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount ${amount}  deposited successfully to account ${self.acc_num}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds. Balance is ${self.balance}")
        else:
            self.balance -= amount
            print(f"Amount ${amount} withdrawn successfully from account ${self.acc_num}")

    def check_balance(self):
        print(f"Balance for account ${self.acc_num} is ${self.balance}")

# data and methods that manipulate the data
gloria_acc = Account("Gloria Atieno", "123456", "987654321", 10000)
don_acc = Account("Don Adams", "12345", "0123456789", 20000)
gloria_acc.deposit(100)
gloria_acc.check_balance()
gloria_acc.withdraw(100)
gloria_acc.check_balance()

don_acc.deposit(1000)
don_acc.check_balance()