class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdrawal = 100
        self.max_withdrawal = 10000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"you have deposited : {amount}")

    def withdraw(self, amount):
        if amount < self.min_withdrawal:
            print(f"tui beda gorib.")
        elif amount > self.max_withdrawal:
            print(f"ato taka kothao nai.")
        else:
            self.balance -= amount
            print(f"here is your money : {amount}")
            print(f"your current balance is : {self.balance}")


brac = Bank(1000)
brac.deposit(5000)

print(brac.get_balance())
