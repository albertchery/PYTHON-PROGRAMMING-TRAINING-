class BankAccount:
    # Constructor
    def __init__(self,balance,name):
        self.name=name
        self.__balance=balance
    # Getters
    def get_balance(self):
        return self.__balance
    # setters
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("INVALID BALANCE AMOUNT")
# Main
account=BankAccount(500,"BAVITH")
print(account.get_balance())       
print(account.set_balance(500))
print("Total after adding",account.get_balance())