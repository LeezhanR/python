# '1 . Map '
A = [5,10,15,20,25,30,35,40,45,50]
divide=lambda  x : x/5
print(list(map(divide,A)))
multiply=lambda x : x*2
print(list(map(multiply,A)))
' 2 . Reduce '
import functools
difference= lambda x,y : x-y
print(functools.reduce(difference,A))
' 3 . Filter '
A = int(input("Enter an number : "))
def prime (A):
    if A==1 or A==0:
        return False  
    else:
        i = 2
        while i < A:
            if A%i==0:
                return False
            break
        i+=1
    return True
print(list(filter(prime,A)))
