from BaseModel import BaseModel

class BaseModelV2(BaseModel):
    
    def __init__(self, dni, name, surname, iban, balance):
        super().__init__(dni, name, surname)
        
        self.__iban = iban
        self.__balance = balance
        self.__stocks = {}
        
    def getIban(self):
        return self.__iban
    def setIban(self, value):
        self.__iban = value
        
    def getBalance(self):
        return self.__balance
    def setBalance(self, value):
        self.__balance = value
        
    def getStocks(self):
        return self.__stocks
    def setStocks(self, stock, cantidad):
        self.__stocks[stock] = cantidad