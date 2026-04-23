class Bank:
    def __init__(self, holder_name, initial_balance):
        self.holder_name = holder_name
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


rif = Bank("Rif", 1000)

rif.deposit(500)
print(rif.get_balance())
