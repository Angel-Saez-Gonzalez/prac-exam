from BankController import BankController

def inputDni():
    dni = input("Input the dni: ")
    return dni

def inputName():
    name = input("Input the name: ")
    return name

def inputSurname():
    surname = input("Input the surname: ")
    return surname

def inputAccount():
    account = input("Input the account: ")
    return account

def inputBalance():
    balance = input("Input the balance: ")
    return float(balance)

ctrl = BankController()

while True:
    print(str(ctrl.getCantPortfolios())+" portfolios")
    print("1.-Add portfolio")
    print("2.-Delete portfolio")
    print("3.-Buy Stock for a client")
    print("4.-Sell stock for a client")
    print("5.-List portfolio portfolio")
    print("6.-Exit")

    option = input("Chhose an option: ")

    if option == "1":
        dni = inputDni()
        name = inputName()
        surname = inputSurname()
        account = inputAccount()
        balance = inputBalance()

        if ctrl.addPortfolio(dni,name,surname,account,balance):
            print("Account created")
        else:
            print("error")

    if option == "2":
        dni = inputDni()
        if ctrl.removePortfolio(dni):
            print("Deleted")
        else:
            print("Not deletes")

    if option == "3":
        dni = inputDni()
        if ctrl.portfolioExists(dni):
            stocks = ctrl.listStocks()
            for stock, values in stocks.items():
                print("Stock key:", stock, " -> ", values)

            stock = input("Select Stock: ")
            quantitity = input("Select quantity:")
            precio = stocks[stock][1]

            if ctrl.buyStock(dni,stock,float(quantitity),float(precio)):
                print("Buyed")
            else:
                print("not buyed")
            

        else:
            print("Dont exist")

    if option == "4":
        pass

    if option == "5":
        dni = inputDni()
        if ctrl.portfolioExists(dni):
            portfolio = ctrl.listPortfolio(dni)
            print("Dni: "+portfolio.getDni())
            print("name: "+portfolio.getName())
            print("Surname: "+portfolio.getSurname())
            print("Account: "+portfolio.getAccount())
            print("Balance: "+str(portfolio.getBalance()))
            for key,value in portfolio.getStocks().items():
                print("Stock: "+key+" quantity: "+str(value))

        else:
            print("Dont exixt")

    if option == "6":
        break