### 1 . Tables
##
##
##A = int(input("Enter the table you want to know : "))
##
##for i in range(1,11,1):
##    print(i,"x",A," = ",i*A)
##    i+=1

# 2 . Sum of list

l = [1,2,3,4,5]
s = 0
for i in l:
    s+=i
    print("The numbers are",s)
print("The Sum of the List is ",s)




### 3 . Length of an string
##
##A = str(input("Enter an string to check the length : "))
##B = len (A)
##for i in range(1,B):
##        print(i,".",A)
##print("The length of the string is :", len(A))
##

### 4 . product of an list
##
##
##A = list(input("Enter an list to find the product :"))
####A = list(map(int,A.split()))
##B = 1
##for i in A :
##        B *= i
##        print("the numbers are :",B)
##print("The product of the list is :",B)


# 5 . Factorial of an number


##A = int(input("Enter an number to find factorial :"))
##B = 1
##for i in range(1,A+1):
##        B*=i
##print("The factorial of the given number is :",B)
##       
##


### 6 . odd or even using
##
##A = int(input("Enter how many numbers of odd and even"))
##
##for i in range(1,A+1):
##        if i%2==0:
##                print("\nEven :",i)
##        else:
##                print("\nOdd : ",i)


### 7 . printing  all the characters of string separately
##
##A = str(input("Enter an string :"))# str is also default 
##for i in A:
##    print(i)
##

# 8 .  iterateing through a list and print even and odd respectively



##A = (input("Enter an list to see odd and even numbers :"))
##A = list(map(int,A.split()))
####A=[1,2,3,4,5]
##
##for B in A:
##    if B%2==0:
##        print("Even :",B)
##    else:
##        print("Odd :",B)
##    

# 9 . printing the vowels from the string


A = input("Enter an word to find the vowels in it :")
B = "a,e,i,o,u,A,E,I,O,U"
for i in A :
    if i in B:
        print("The vowels in the given word is :",i)






