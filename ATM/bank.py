
class Bank:
    transaction_cost = 0.8
    transaction_country = 'Other'

    def __init__(self, name, balance ,bank):
        self.name = name
        self.balance = balance
        self.bank = bank

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print('You do not have sufficient funds')
        else:
            self.balance -= withdraw_amount
            self.balance -= self.transaction_cost
            print(self.balance)
            return self.balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(self.balance)
        return self.balance


class SABank(Bank):
    transaction_cost = 0.5  # Although I Call super Class, the transaction cost gets overridden
    transaction_country = 'South Africa'

    def __init__(self, name, balance, bank):
        super().__init__(name, balance, bank)

    def withdraw(self, withdraw_amount):
        super().withdraw(withdraw_amount)

    def deposit(self, deposit_amount):
        super().deposit(deposit_amount)


class NetBank(SABank):
    transaction_cost = 1

    def __init__(self, name, balance, bank):
        super().__init__(name, balance, bank)

    def withdraw(self, withdraw_amount):
        super().withdraw(withdraw_amount)

    def deposit(self, deposit_amount):
        super().deposit(deposit_amount)


class Capitec(SABank):
    transaction_cost = 0.2

    def __init__(self, name, balance, bank):
        super().__init__(name, balance, bank)

    def withdraw(self, withdraw_amount):
        super().withdraw(withdraw_amount)

    def deposit(self, deposit_amount):
        super().deposit(deposit_amount)
