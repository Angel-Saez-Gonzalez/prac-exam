import random

class Event():
    def __init__(self, name, date, location, province, regprice):
        self._name = name
        self._date = date
        self._location = location
        self._province = province
        self._regprice = regprice
        self._total = 0
        self._finished = False
        self._participants = []
        self._podium = {}
        
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name
        
    def getDate(self):
        return self._date
    def setDate(self, date):
        self._date = date
        
    def getLocation(self):
        return self._location
    def setLocation(self, location):
        self._location = location
        
    def getProvince(self):
        return self._province
    def setProvince(self, province):
        self._province = province
        
    def getRegPrice(self):
        return self._regprice
    def setRegPrice(self, regprice):
        self._regprice = regprice
    
    def getTotal(self):
        return self._total
    def setTotal(self, total):
        self._total = total
        
    def getFinished(self):
        return self._finished
    def setFinished(self):
        self._finished = True
        
    def getParticipants(self):
        return self._participants
    def addParticipants(self, dni, name, age, email):
        self._participants.append((dni, name, age, email))
        
    def getPodium(self):
        return self._podium
    def setPodium(self):
        par = self._participants
        
        x = random.randint(0, len(par))
        self._podium["First"] = par[x]
        par.remove(x)
        j = random.randint(0, len(par))
        self._podium["Second"] = par[j]
        par.remove(j)
        k = random.randint(0, len(par))
        self._podium["Third"] = par[k]
        par.remove(k)