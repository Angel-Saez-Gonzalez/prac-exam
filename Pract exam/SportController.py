from SportModel import Event

class SportController():
    def __init__(self):
        self.events = {}

    def addEvent(self, name,date,location,province,price):
        if self.eventExists(name):
            return False
        else:
            event = Event(name,date,location,province,price)
            self.events[name] = event
            return True
    
    def addParticipants(self,nameEvent,dni,name,age,email):
        if self.eventExists(nameEvent):
            self.events[nameEvent].setParticipants(dni,name,age,email)
            return True
        else:
            return False

    def eventExists(self,name):
        if name in self.events.keys():
            return True
        else: 
            return False