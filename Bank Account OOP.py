class bankAccount():
    
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def withdraw(self, wdAmnt):
        if self.balance >= wdAmnt:
            self.balance = self.balance - wdAmnt
            print('Withdrawal was completed')
        else:
            print('Funds not avavlaible')
    
    def  deposit(self,depAmnt):
        self.balance = self.balance + depAmnt
        print('Deposit was accepted')
    
    def __repr__(self):
        return f'Account Name: {self.owner}, Account Balance: {self.balance}'
    
Account1 = bankAccount('Taiwo',3400)

print(Account1)
Account1.deposit(30)
Account1.withdraw(300)
Account1.balance
