from this import d
from BaseModelV2 import BaseModelV2
import json, requests

class BankController():
    def __init__(self):
        self.__accounts = {}
        
    def getAcc(self, dni):
        return self.__accounts[dni]

    def getAccounts(self):
        return len(self.__accounts)

    def addPortfolio(self, dni, name, surname, iban, balance):
        v = BaseModelV2(dni, name, surname, iban, balance)
        if dni not in self.__accounts:
            self.__accounts[dni] = v
            return v
        else:
            return False

    def delPortfolio(self, dni):
        if dni in self.__accounts:
            return self.__accounts.pop(dni)
                
    
    def listPortfolio(self, dni):
        for key in self.__accounts:
            if(key == dni):
                return self.__accounts[key]
        return False
    
    def listStocks(self):

        url = "https://bb-finance.p.rapidapi.com/market/get-full"
        querystring = {"id":"ANA:SM,ACX:SM,ACS:SM,SAN:SM,BBVA:SM,CABK:SM,CLNX:SM,ENG:SM,ELE:SM,FER:SM,GRF:SM,IAG:SM,IBE:SM,ITX:SM,IDR:SM,MAP:SM,MEL:SM,NTGY:SM,REP:SM,TEF:SM"}
        headers = {
            'x-rapidapi-host': "bb-finance.p.rapidapi.com",
            'x-rapidapi-key': "a365ad1a8cmsh8c4907a923c8b44p1ddecajsn2ec4d759c257"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)

        stocks = {}
        for stock, values in data["result"].items():
            stocks[stock] = (values["name"], values["last"])
            
        return stocks
        
    def buyStock(self, dni, stock, quantity, stocks):
        if dni in self.__accounts:
            cliente = self.__accounts[dni]
            if stock in stocks:
                valor = float(stocks[stock][1])
                if (quantity*valor) <= cliente.getBalance():
                    cliente.setStocks(stock, quantity)
                    cliente.setBalance(cliente.getBalance() - quantity*valor)
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def sellStock(self, dni, stock, quantity, stocks):
        if dni in self.__accounts:
            cliente = self.__accounts[dni]
            if stock in cliente.getStocks():
                valor = float(stocks[stock][1])
                if(quantity <= int(cliente.getStocks()[stock])):
                    cliente.setStocks(stock, (int(cliente.getStocks()[stock]) - quantity))
                    cliente.setBalance(cliente.getBalance() + (valor*quantity))
            else:
                return False
        else:
            return False