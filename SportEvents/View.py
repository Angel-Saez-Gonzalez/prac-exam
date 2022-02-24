from Controller import Controller

ctrl = Controller()

def inputName():
    return input("Input the event Name: ")

def inputDate():
    return input("Input the event Date: ")
    
def inputLocation():
    return input("Input the event Location: ")
    
def inputProvince():
    return input("Input the event Province: ")
    
def inputRegPrice():
    return input("Input the event Registration Price: ")
    
def inputDni():
    return input("Input the participant Dni: ")
    
def inputParticipantName():
    return input("Input the participant Name: ")
    
def inputAge():
    return input("Input the participant Age: ")
    
def inputEmail():
    return input("Input the participant Email: ")

while True:
    print("1.- Add Event")
    print("2.- Add participant to an event")
    print("3.- List pending events with participants")
    print("4.- List events finished with podium")
    print("5.- Finish an event with 3 random participants")
    print("6.- Exit")
    option = int(input("Elige una opcion: "))
    
    if option == 1:
        name = inputName()
        date = inputDate()
        location = inputLocation()
        province = inputProvince()
        regPrice = inputRegPrice()
        
        ctrl.addEvent(name, date, location, province, regPrice)
        
    if option == 2:
        eventname = inputName()
        
        dni = inputDni()
        name = inputParticipantName()
        age = inputAge()
        email = inputEmail()
        
        ctrl.addParticipant(eventname, dni, name, age, email)
        
    if option == 3:
        pending = ctrl.getPendingEvents()
        
        if len(pending) == 0:
            print("No hay eventos")
        else:
            for x in range(len(pending)):
                for event in pending:
                    print("Current Event ", x+1)
                    print("     Nombre: " + event.getName())
                    print("     Date: " + event.getDate())
                    print("     Location: " + event.getLocation())
                    print("     Province: " + event.getProvince())
                
    if option == 4:
        finished = ctrl.getFinishedEvents()
        
        if len(finished) == 0:
            print("No hay eventos")
        else:
            for x in range(len(finished)):
                for event in finished:
                    print("Finished Event", x+1)
                    print("     Nombre: " + event.getName())
                    print("     Date: " + event.getDate())
                    print("     Location: " + event.getLocation())
                    print("     Province: " + event.getProvince())
                
    if option == 5:
        eventname = inputName()
        
        