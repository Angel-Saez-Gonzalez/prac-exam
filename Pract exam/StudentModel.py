
class Student():
    def __init__(self,dni,name,surname,age,city,province,email):
        self._dni = dni
        self._name = name
        self._surname = surname
        self._age = age
        self._city = city
        self._province = province
        self._email = email
    
    def getDni(self):
        return self._dni
    def setDni(self,dni):
        self._dni = dni

    def getName(self):
        return self._name
    def setName(self,name):
        self._name = name
    
    def getSurname(self):
        return self._surname
    def setSurname(self,surname):
        self._surname = surname
    
    def getAge(self):
        return self._age
    def setAge(self,age):
        self._age = age
    
    def getCity(self):
        return self._city
    def setCity(self,city):
        self._city = city
    
    def getProvince(self):
        return self._province
    def setProvince(self,province):
        self._province = province
    
    def getEmail(self):
        return self._email
    def setEmail(self,email):
        self._email = email
