from random import *
from os import *
def Fun(a,file):
    c = randint(1,11)
    if a==c:
        print("Your file is safe !!")
    else:
        Sugession = input("Enter yes to remove the file permanently (Yes (or) No) :")
        if Sugession=="Yes":
            remove(file)
        else:
            print("Your file is not deleted !!")
a = int(input("Enter a positive number betwen 1-10:"))
file = input("Enter an file name or the path of the file :")
Fun(a,file)

