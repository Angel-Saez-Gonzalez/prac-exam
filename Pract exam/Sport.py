
import email
from re import A
from SportController import SportController

def inputName():
    return input("Input the event Name: ")

def inputDate():
    return input("Input the event Date: ")
    
def inputLocation():
    return input("Input the event Location: ")
    
def inputProvince():
    return input("Input the event Province: ")
    
def inputPrice():
    return input("Input the event Registration Price: ")
    
def inputDni():
    return input("Input the participant Dni: ")
    
def inputParticipantName():
    return input("Input the participant Name: ")
    
def inputAge():
    return input("Input the participant Age: ")
    
def inputEmail():
    return input("Input the participant Email: ")

ctrl = SportController()

while True:
    print("1-add Event")
    print("2-add participant to an event")
    print("3-List pending events")
    print("4-Lis events finished")
    print("5-Finish ecent")
    print("0-Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        name = inputName()
        date = inputDate()
        location = inputLocation()
        province = inputProvince()
        price = inputPrice()

        if ctrl.addEvent(name,date,location,province,price) == True:
            print("Evrnt added")
        else:
            print("The event Exists")
    
    if option == 2:
        nameEvent = inputName()
        name = inputName()
        dni = inputDni()
        age = inputAge()
        email = inputEmail()

        if ctrl.addParticipants(nameEvent,dni,name,age,email) == True:
            print("Participant added")
        else:
            print("Not added")

    if option == 3:
        A

    if option == 4:
        A

    if option == 5:
        A

    if option == 0:
        break