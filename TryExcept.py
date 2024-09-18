def CheckAge(n):
    if n<0 or n>120:
        raise Exception ()
    print("Thank you for giving your age")
try :
    CheckAge(130)
except :
    print("Enter an age between 0 and 120 ")
# Types of Exceptions  
# 1 . SyntaxError
try:
    exec('if True print("Hello")') 
except SyntaxError as s:
    print(f"SyntaxError : {s}, check and change it")
# 2 . TypeError
try :
    "A"+1
except TypeError as t:
    print(f"TypeError : {t} , Give only integer data type for a")
# 3 . NameError
try :
    print(a)
except NameError as n:
    print(f"NameError :  {n} , Give the correct value in print statment")
# 4 .IndexError 
try :
    a=[1,2,3,4,5]
    print(a[5])
except IndexError as i:
    print(f"IndexError : {i} , Give the correct index")
# 5 . KeyError
try :
    d={"a":1}
    print(d["b"])
except KeyError as k:
    print(f"KeyError : {k} ,key does not exists:Give the correct which exists in the dictionary")
# 6 . ValueError
try :
    a=int(input("Enter an number :"))
except ValueError as v:
    print(f"ValueError : {v} , Give only int data type ")
# 7 . AttributeError
try:
    d.append("a")
except AttributeError as a:
    print(f"AttributeError : {a} , Give the correct method for dictionary")
# 8 . ZeroDivitionError
try :
    print(2/0)
except ZeroDivisionError as z:
    print(f"ZeroDivitionError : {z} , Zero can not be as denomenator")
else:
    print("Any thing divided by zero is Infinity")
# 9 . ImportError
try:
    import numpy 
except ImportError as I:
    print(f"ImportError : {I} , Give an existing library ")
finally:
    print("All Errors have been captured successfully!!")