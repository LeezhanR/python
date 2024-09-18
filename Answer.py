from Tasks import *
'1 . Find the squares of all items from the list'
print(" 1 . ",list(map(Square,l)))
'2 . filter even and odd numbers from the list'
print(" 2 . ",list(filter(Odd,l)))
print(" 2 . ",list(filter(Even,l)))
'3 . map "even" on even numbers and "odd" for odd numbers in the list'
print(" 3 . ",list(map(lambda l : "even" if l % 2 == 0 else "odd",l)))
'4 . find the product of all numbers from the list'
print(" 4 . ",reduce(Product,l))
'5 . Convert List of Strings to Uppercase using map'
print(" 5 . ",list(map(Uppercase,word)))
'6 . Find the cummulative difference of all items in the list'
print(" 6 . ",list(accumulate(l,difference)))
'7 . Filter Words Starting with "b"'
print(" 7 . ",list(filter(f,words)))
'8 . find the factorial of a number using reduce'
print(" 8 . ",reduce(Product,l))
'9 . filter prime numbers from the list'
print(" 9 . ",list(filter(prime,l)))