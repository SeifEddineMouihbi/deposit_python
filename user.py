class userName:

    def __init__(self, name):
        self.name = name
        self.credit = 0

    def deposit(self, credit):
        self.credit += credit

    def withdraw(self, credit):
        self.credit -= credit

    def accountInfo(self):
        print ("account username : %s" %self.name, "and balance : %d" %self.credit)
    
    def transfer(self,credit,userName):
        self.credit -= credit
        userName.credit += credit
        self.accountInfo()
        userName.accountInfo()

john = userName("john")
maria = userName("Maria")
leila = userName("Leila")

john.deposit(150)
john.deposit(250)
john.deposit(300)
john.withdraw(275)
john.accountInfo()


maria.deposit(200)
maria.deposit(50)
maria.withdraw(250)
maria.withdraw(150)
maria.accountInfo()

leila.deposit(150)
leila.withdraw(100)
leila.withdraw(300)
leila.withdraw(100)
leila.accountInfo()

john.transfer(100,leila)