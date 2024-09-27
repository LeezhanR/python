# Bank Account
# Details

class Bank:
    def __init__(self,Balance=0):
        self.__Balance = Balance
    def Deposit(self,Deposit):
        if Deposit<=0:
            print("Enter the valid amount to deposit")
        else:
            self.__Balance+=Deposit
    def Withdraw(self,Withdraw):
        if self.__Balance>=Withdraw:
            self.__Balance-=Withdraw
        else:
            print(f"Enter the amount from your Balance of {self.__Balance}")
    def Check_Balance(self):
        return self.__Balance

Account = Bank(1000)
Account.Deposit(1000)
Account.Withdraw(500)
print(Account.Check_Balance())

