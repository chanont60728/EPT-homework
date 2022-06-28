class Account():
    def __init__(self,id:str,name:str,surname:str,balance:float):
        self.id = id
        self.name = name
        self.surname = surname
        self.balance = balance
    
    def getFullname(self):
        return self.name+" "+self.surname
    
    # set money as at latest
    def setBalance(self,set_money:float):
        self.balance = set_money
    
    # show balance 
    def getBalance(self):
        return self.balance
    
    # add to setBalance:
    def deposit(self,deposit_money:float):
        self.balance = self.balance+deposit_money
    
    # minus to setBalance:
    def withdraw(self,withdraw_money:float):
        if self.balance>=withdraw_money:
            self.balance = self.balance-withdraw_money

    @staticmethod
    def transfer(source_account,destination_account,money_transfer:float):
        if source_account.balance>=money_transfer:
            source_account.withdraw(money_transfer)
            destination_account.deposit(money_transfer)
        return print(source_account.getFullname() + "\n" + str(source_account.getBalance()) + "\n" + destination_account.getFullname() + "\n" + str(destination_account.getBalance()))



