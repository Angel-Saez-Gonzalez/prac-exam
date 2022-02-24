from Event import Event

class Controller():
    
    def __init__(self):
        self.events = {}      
        
    def addEvent(self, name, date, location, province, regprice):
        event = Event(name, date, location, province, regprice)
        self.events[name] = event
        
    def addParticipant(self, eventname, dni, name, age, email):
        if self.events[eventname]:
            self.events[eventname].addParticipants(dni, name, age, email)
            
        else:
            return None
        
    def getPendingEvents(self):
        pending = []
        for event in self.events.values():
            if len(event.getParticipants()) > 0 and event.getFinished() == False:
                pending.append(event)
        return pending
    
    def setPodium(self, eventname):
        if self.events[eventname]:
            self.events[eventname].setPodium()
            self.events[eventname].setFinished()
            
    def getFinishedEvents(self):
        finished = []
        for event in self.events.values():
            if event.getFinished() == True and len(event.getPodium()) == 3:
                finished.append(event)
        return finished