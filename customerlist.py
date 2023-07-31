from bank import Bank, SABank, NetBank


# here we are withdrawing an amount from all the class objects.
# it has been set up so that you can add more customers to the list,
# and it will include the additional customer in the calculation

# customer_name = objectlist[0].name
# print(customer_name)
# for i in range(0, len(namelist)):
#    objectlist[i].withdraw(100)

class SignUp:
    namelist = ['Janco', 'Ben', 'Jannet', "Chris"]
    balancelist = [1000, 200, 500, 5000]
    banklist = ['NetBank', 'Capitec', 'ABSA', "ABN"]
    objectlist = []

    def __init__(self, name, deposit, bank):
        self.name = SignUp.namelist.append(name)
        self.deposit = SignUp.balancelist.append(deposit)
        self.deposit = SignUp.banklist.append(bank)

    # Creates the Object
    if len(namelist) == len(balancelist):
        for i in range(0, len(namelist)):
            objectlist.append(Bank(namelist[i], balancelist[i], banklist[i]))
    else:
        print("Namelist not the same len as balance list")
