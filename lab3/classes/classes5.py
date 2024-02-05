class Bank_Account():

    def __init__(self, owner = 'Sam', balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print ('Withdrawal failed.')
        else:
            self.balance -= amount
            print ('Withdrew', amount, 'dollars. New balance:', self.balance, 'dollars.')

Myaccount = Bank_Account()
Myaccount.deposit(1000)
Myaccount.withdraw(5000)
Myaccount.withdraw(500)