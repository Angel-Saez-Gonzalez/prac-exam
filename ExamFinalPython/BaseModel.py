class BaseModel():
    def __init__(self,dni,name,surname):
        self.__dni = dni
        self.__name = name
        self.__surname = surname
        
    def getDni(self):
        return self.__dni
    def setDni(self,dni):
        self.__dni = dni
    
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
    
    def getSurname(self):
        return self.__surname
    def setSurname(self,surname):
        self.__surname = surname
     