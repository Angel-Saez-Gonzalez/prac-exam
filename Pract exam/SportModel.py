

import random


class Event():
    def __init__(self,name,date,location,province,price):
        self._name = name
        self._date = date
        self._location = location
        self._province = province
        self._price = price
        self._total = 0
        self._participants = []
        self._finished = False
        self._podium = {}

    def getName(self):
        return self._name
    def setName(self,name):
        self._name = name

    def getDate(self):
        return self._date
    def setDate(self,date):
        self._date = date
    
    def getLocation(self):
        return self._location
    def setLocation(self,location):
        self._location = location
    
    def getProvince(self):
        return self._province
    def setProvince(self,province):
        self._province = province

    def getPrice(self):
        return self._price
    def setPrice(self,price):
        self._price = price

    def getTotal(self):
        return self._total
    def setTotal(self,total):
        self._total = total

    def getParticipants(self):
        return self._participants
    def setParticipants(self,dni,name,age,email):
        self._participants.append((dni,name,age,email))
    
    def getFinished(self):
        return self._finished
    def setFinished(self):
        self._finished = True
    
    def getPodium(self):
        return self._podium
    def setPodium(self):
        partici = self._participants
        
        x = random.randint(0, len(partici))
        self._podium["First"] = partici[x]
        partici.remove(x)
        j = random.randint(0, len(partici))
        self._podium["Second"] = partici[j]
        partici.remove(j)
        k = random.randint(0, len(partici))
        self._podium["Third"] = partici[k]
        partici.remove(k)