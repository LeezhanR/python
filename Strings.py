### 1. counting vowels in an string
##
##a = input("Enter an string :")
##b = "aeiouAEIOU"
##c = 0
##for i in a:
##    if i in b:
##        c+=1
##print(f"The number of vowels in the given string is : {c}")\


#### 2 .Printing the string in reverse
####
####a = input("Enter an string :")
####b = len(a)
####c = ""
####for i in range(b - 1,-1,-1):
####    c+=a[i]
####print(c)
####

#### 3 . removing duplicate letters from the string
####
####a = input("Enter an string :")
####b = len(a)
####c = ""
####for i in range (b):
####    if a[i] in c:
####        continue
####    else:
####        c+=a[i]
####print(f"The result after removing duplicate letters is : {c}")

##
### 4 .checking occurance
##
##a = input ("Enter an string :")
##b = input("Enter an letter to check the occurance :")
##c = 0
##for i in a :
##    if i == b :
##        c+= 1
##print(f"the letter {b} is occuring {c} in the string {a}")
    
##
### 5 . palindrome checking
##
##
##a = input("Enter an string :")
##b = len(a)
##c = ""
##for i in range(b - 1,-1,-1):
##    c+=a[i]
##if a == c :
##    print("the given string is an palindrome")
##else :
##    print("The given string is not an palindrome")
##
##
# 6 . counting words

a = input("Enter an sentance :")
a= a.split(" ")
b= 0
for i in a :
    b+=1
print(b)


# 7 . 
    

a = input ("Enter an sentence :")
a = a . capitalize()
print(a)























