### 1 . Adding numbers
##
##def add_number(a,b):
##    print(f"The sum of two numbers : {a} and {b} is {a+b}")
##a=int(input("Enter the first number : "))
##b = int(input("Enter the second number : "))
####add_number(a,b)

### 2 . Prime number check
##
##def is_prime(n):
##    if n==1 or n==0:
##        print(n,"is neither prime nor composite")    
##    else:
##        i = 2
##        while i < n:
##            if n%i==0:
##                print(n," is not an prime number ")
##                break
##            i+=1
##            print(n," is an prime number")
##
##n = int(input("Enter an number : "))
##
##is_prime(n)

### 3 . Factorial
##
def factorial(n):
   if n==0 or n==1:
       return 1
   return n * factorial(n-1)
n = int(input("Enter an number for factorising :"))
fact=factorial(n)
print(f"The factorial of {n} is {fact}")

### 4 . Reversing string
##
##def reverse_string(s):
##    if len(s)==0:
##        return s
##    return reverse_string(s[1:])+s[0]
##s = input("Enter a string : ")
##b=reverse_string(s)
##print(f"The string {s} after reversing is {b}")

# 5 . finding max of an number

def find_max(m):
    checking = m[0]
    for i in m:
        if i>checking:
            checking = i
    return checking
m = input("Enter an list to find the maximum value :")
m = m.split(",")
Result = find_max(m)
print(f"The maximum number from : {m} is {Result}")




























