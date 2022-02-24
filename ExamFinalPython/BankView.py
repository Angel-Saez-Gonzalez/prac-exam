from BankController import BankController
import re

def inputDni():
    while True:
        dni = input("Intrduce el dni: ")
        print("Dni valido!")
        return dni
            
def inputName():
    while True:
        name = input("Introduce el nombre: ")
        if(name.isalpha() and len(name) > 0):
            print("Nombre correcto!")
            return name
        else:
            print("Nombre incorrecto!")
            
def inputSurname():
    while True:
        surname = input("Introduce apellido: ")
        if(surname.isalpha() and len(surname) > 0):
            print("Apellido correcto!")
            return surname
        else:
            print("Apellido incorrecto!")
        
def inputBalance():
    while True:
        try:
            balance = float(input("Input initial Balance: "))
            if balance >= 0:
                print("Correct balance!")
                return balance
            else:
                print("Incorrect balance!")
        except:
            print("Error! The balance should be positive!")

def inputIban():
    return input("Introduce el iban: ")
    """while True:
        
        if iban != 28:
            print("Format is ESXX-24 digits!")
            continue
        
        españa = iban[0:2]
        code = int(iban[2:4])
        numbers = iban[4:]
        
        if españa != "ES":
            print("Debe de empezar por ES!")
            continue
            
        if numbers.isdigit() == False:
            print("The iban is not correct!")
            continue
        
        fullIban = int(numbers + "142800")
        modul = fullIban % 97
        finalcode = 98 - modul
        
        if finalcode == code:
            return iban
        else:
            print("Error! The iban is not correct!")"""
            
ctrl = BankController()

while True:
    print("Currently there are", ctrl.getAccounts(), "portfolios registered!")
    print("1.- Add a portfolio")
    print("2.- Delete portfolio")
    print("3.- Buy stock for a client")
    print("4.- Sell stock for a client")
    print("5.- List client portfolio")
    print("6.- Exit")
    
    option = int(input("Choose option: "))
    
    if option == 6:
        break
    
    if option == 1:
        dni = inputDni()
        name = inputName()
        surname = inputSurname()
        iban = inputIban()
        balance = inputBalance()
        
        ctrl.addPortfolio(dni, name, surname, iban, balance)
        
    if option == 2:
        dni = inputDni()
        
        cliente = ctrl.delPortfolio(dni)
        
        print("Se ha borrado el cliente: \nDni: " + cliente.getDni() + "\nNombre: " + cliente.getName() + "\nApellido: " + cliente.getSurname() + "\nIban: " + str(cliente.getIban()) + "\nBalance: " + str(cliente.getBalance()) + "\n")
        
    if option == 3:
        dni = inputDni()
        stocks = ctrl.listStocks()
        
        for key, x in stocks.items():
            print("Key: " + str(key) + " : " + str(x) + "\n")
            
        stock = input("Que accion quieres comprar: ")
        quantity = int(input("Cantidad: "))
        
        ctrl.buyStock(dni, stock, quantity, stocks)
        
    if option == 4:
        dni = inputDni()
        cliente = ctrl.getAcc(dni)
        for key, x in cliente.getStocks().items():
            print("Key: " + str(key) + " : " + str(x) + "\n")
            
        stock = input("Introduce el stock: ")
        quantity = int(input("Cantidad que deseas vender: "))
        
        ctrl.sellStock(dni, stock, quantity, ctrl.listStocks())
    
    if option == 5:
        dni = inputDni()
        cliente = ctrl.listPortfolio(dni)
        if(cliente != False):
            print("\nDni: " + cliente.getDni() + "\nNombre: " + cliente.getName() + "\nApellido: " + cliente.getSurname() + "\nIban: " + str(cliente.getIban()) + "\nBalance: " + str(cliente.getBalance()) + "\n")
            
            print("Stocks: ")
            for st, m in cliente.getStocks().items():
                print("     " + str(st) + ": " + str(m))
        else:
            print("No se ha encontrado el cliente!")       