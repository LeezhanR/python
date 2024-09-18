#Creating an normal lambda function
a = lambda x:x+20
print(a(10))
#Input from user
a = lambda x:x+20
x = int(input("Enter a number : "))
print(a(x))
#Two variabls
a = lambda x,y:x*y
x = int(input("Enter a first number : "))
y = int(input("Enter a second number : "))
print(a(x,y))
#Squaring an number by using def function for lambda
def square(n):
  return lambda x : x ** n
squared_num = square(2)
x = int(input("Enter a number to square : "))
print(squared_num(x))