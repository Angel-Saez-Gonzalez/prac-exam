

from StudentController import StudentController

def inputDni():
    dni = input("Input the dni: ")
    return dni

def inputName():
    name = input("Input the name: ")
    return name

def inputSurname():
    surname = input("Input the surname: ")
    return surname

def inputAge():
    age = input("Input the age: ")
    return age

def inputCity():
    city = input("Input the city: ")
    return city

def inputProvince():
    province = input("Input the province: ")
    return province

def inputEmail():
    email = input("Input the email: ")
    return email

ctrl = StudentController()
while True:
    print("1.-Add a student")
    print("2.-Delete a student")
    print("3.-Modify a student")
    print("4.-Search a student")
    print("5.-Exit")

    option = input("Choose an option: ")

    if option == "1":
        dni = inputDni()
        name = inputName()
        surname = inputSurname()
        age = inputAge()
        city = inputCity()
        province = inputProvince()
        email = inputEmail()

        if ctrl.addStudent(dni,name,surname,age,city,province,email):
            print("Added")
        else:
            print("Not added")

    if option == "2":
        dni = inputDni()

        if ctrl.deleteStudent(dni):
            print("Deleted")
        else:
            print("Not deleted")

    if option == "3":
        dni = inputDni()
        if ctrl.studentExists(dni):
            print("1.-Modify a name")
            print("2.-Modify a surname")
            print("3.-Modify a age")
            print("4.-Modify a city")
            print("5.-Modify province")
            print("6.-Modify email")

            choose = input("Coose what you want to modify: ")
            if int(choose)<0 or int(choose)>7:
                print("Mal")
            else:
                newValue = input("Input the newValue: ")
                if ctrl.modifyStudent(dni,choose,newValue):
                    print("Studehnt modified")
                else:
                    print("Not modified")
        else:
            print("The student noexist")

    if option == "4":
        dni = inputDni()
        if ctrl.studentExists(dni):
            student = ctrl.searchStudent(dni)
            print("Student name: "+student.getName()+" Surname: "+student.getSurname())

    if option == "5":
        break