"""""
This is an object oriented programming example."
It demonstates the concepts of inheritance , encapsulation, data"
"""

#
class BankAccount:
    #Constructor
    def __init__ (self, account_holder, balance):
        self.account_holder= account_holder #Public attribute
        self.__balance = balance #Private attribute (Encapsulation)

    #deposit () method     
    def deposit (self , amount ):
        """""Allows deposit of money into the account to add to the hidden balance attribute"""
        if amount > 0:
            self.__balance += amount
            print (f"Depostited {amount}, New balance : {self.__balance}")
        else:
            print ("Deposit amount must be positive")
    
    #Withdraw () nethod 
    def withdraw(self,amount):
        """" Allows withdrawal of money into the account to reduce the hidden balance attribute """
        if (0< amount <= self.__balance):
            self.__balance -= amount 
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")
        

    #get_balance () method 
    def get_balance(self):
        """""Allows viewing of balance (getter method)"""
        return self.__balance

#end of parent class BankAccount

#We will now create child classes that inherit from the parent BankAccount

##INHERITANCE##
#Child class SavingsAccount
class SavingsAccount (BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        """Child constructor which uses the parent but also adds an attribuute interest_rate"""
        super().__init__(account_holder, balance ) #call the parent constructor to define and set
        self.interest_rate = interest_rate # public attribute

    def apply_interest(self):
        """""SavingsAccount have a unique method that applies interest to the balance"""
        interest = self.get_balance() * self.interest_rate/100
        self.deposit(interest)
        print(f"Interest of {interest} applied. New balance: {self.get_balance()}")

#child class CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        """""Child constructor which uses the parent but also adds an attribuute interest_rate"""
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit


    def withdraw (self, amount): 
        """Polymorphism applied by having a child withdraw() class overide method the parent withdraw() method"""

        if amount <= self.get_balance() + self.overdraft_limit:
            self.deposit(-amount) #we will deposit a negaitive amount indicating an overdraft
            print(f"Overdraft allowed.Withdrawn: {amount}. Remaining balance: {self.get_balance()}")
        else:
            print("Withrdawal exceeds overdraft limit.")
    

#Actual program 
savings = SavingsAccount("John", 1000, 5) #created John's Account with 1,000 balance and 5% interest rate
checking = CheckingAccount("John", 500, 200) #created John's Account with 500 balance and 200 overdraft limit

savings.deposit(500) 
savings.apply_interest()

checking.withdraw(900)
checking.withdraw(200)

