from BankModel import BankModel
import requests, json

class BankController():
    def __init__(self):
        self._portfolio = {}

    def getCantPortfolios(self):
        return len(self._portfolio)

    def portfolioExists(self,dni):
        if dni in self._portfolio.keys():
            return True
        else: return False

    def addPortfolio(self,dni,name,surname,account,balance):
        if self.portfolioExists(dni):
            return False
        else: 
            p = BankModel(dni,name,surname,account,balance)
            self._portfolio[dni] = p
            return True
    
    def removePortfolio(self,dni):
        if self.portfolioExists(dni):
            if len(self._portfolio[dni].getStocks()) > 0:
                return False
            else:
                del self._portfolio[dni]
                return True
        else: return False

    def listPortfolio(self,dni):
        if self.portfolioExists(dni):
            return self._portfolio[dni]
        else: return False

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
        #print("List of stocks")
        #print("--------------")
        for stock, values in data["result"].items():
        #    print("Stock key:", stock, " -> ", values["name"], "Price: ", values["last"])
            stocks[stock] = (values["name"], values["last"])
        
        #stock = input("Select stock:")
        #print(stock, stocks[stock][0], stocks[stock][1])
        return stocks 

    def buyStock(self, dni, stock,quantity, precio):
        if self.portfolioExists(dni):
            preciototal = quantity*precio
            if self._portfolio[dni].getBalance() < preciototal:
                return False
            else: 
                newBalance =  float(self._portfolio[dni].getBalance()) - float(preciototal)
                self._portfolio[dni].setBalance(float(newBalance))
                self._portfolio[dni].setStocks(stock,quantity)
                return True
        else: return False