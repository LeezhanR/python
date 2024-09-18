'Tasks'
# 1 . Find the squares of all items from the list
l = [1,2,3,4,5,6,7,8,9,10]
Square = lambda  x : x**2
print(list(map(Square,l)))

# 2 . filter even and odd numbers from the list
l = [1,2,3,4,5,6,7,8,9,10]
Odd = lambda x : x%2!=0
Even = lambda x : x%2==0
print(list(filter(Odd,l)))
print(list(filter(Even,l)))

# 3 . map "even" on even numbers and "odd" for odd numbers in the list
print(list(map(lambda l : "even" if l % 2 == 0 else "odd",l)))
# 4 . find the product of all numbers from the list
from functools import *
Product= lambda x,y : x*y
print(reduce(Product,l))
# 5 . Convert List of Strings to Uppercase using map
word = ['apple', 'banana', 'cherry']
def Uppercase(word):
    return word.upper()

print(list(map(Uppercase,word)))
# 6 . Find the cummulative difference of all items in the list
from itertools import *
difference = lambda x,y : x-y
print(list(accumulate(l,difference)))
# # 7 .  Filter Words Starting with "b"
words = ['apple', 'banana', 'cherry', 'blueberry', 'kiwi']
f = lambda x : x if x[0]=='b' else False
print(list(filter(f,words)))
# 8 .  find the factorial of a number using reduce
Product= lambda x,y : x*y
print(reduce(Product,l))
# # 9 .  filter prime numbers from the list
def prime (l):
    if l==1 or l==0:
        return False  
    else:
        i = 2
        while i < l:
            if l%i==0:
                return False
            break
        i+=1
    return True
print(list(filter(prime,l)))

    






