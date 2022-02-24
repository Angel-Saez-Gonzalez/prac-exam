from BaseModel import *

class BankModel(BaseModel):
    def __init__(self,dni,name,surname,account,balance):
        super().__init__(dni,name,surname)
        self._account = account
        self._balance = float(balance)
        self._stocks = {}

    
    def getAccount(self):
        return self._account
    def setAccount(self,account):
        self._account = account

    def getBalance(self):
        return self._balance
    def setBalance(self,balance):
        self._balance = balance
    
    def getStocks(self):
        return self._stocks
    def setStocks(self,stock,quantity):
        self._stocks[stock] = quantity
