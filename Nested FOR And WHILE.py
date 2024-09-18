### 1. Tables(using nested for loop)
##
##for i in range(1,6):
##    print(i,"TABLE")
##    print("---------")
##    for j in range(1,11):
##        print(j,"x",i,"=",i*j)
##    print("-"*15)
##
### 2 . Tables(using nested while loop)
##
##i = 0
##while i<5:
##    i+=1
##    print(i,"TABLE")
##    print("--------")
##    j = 1
##    while j<=10:
##        print(j,"x",i,"=",i*j)
##        j+=1
##    print("-"*15)
##
##
### 3 .  using control statment
##
##
##for i in range(1,20):
##    if i==12:
##        pass
##    elif i%2==0:
##        print(i,"is even")
##    elif i>=15:
##        break
##    elif i%2!=0:
##        continue

### 4 . Find the prime number


A = int(input("Enter an number :"))
if A==1 or A==0:
   print(A,"is neither prime nor composite")    
else:
   i = 2
   while i < A:
       if A%i==0:
           print(A," is not an prime number ")
           break
       i+=1
   print(A," is an prime number")

# 5 . patterns using loop
# (i) Right angled triangle

##
##for i in range (7):
##    print("*",end=" ")
##    for j in range (1,i+1):
##        print("*",end=" ")
##    print()
        
    
### (ii) Left angled triangle
##
##for i in range (1,10):
##    for j in range(11-i):
##        print(" ",end=" ")
##    for k in range (i):
##        print("*",end=" ")
##    print()


##
### (iii) Half Diamond
##
##for i in range (7):
##    print("*",end=" ")
##    for j in range (1,i+1):
##        print("*",end=" ")
##    print()
##for k in range(7,1,-1):
##    for l in range(k-1,0,-1):
##        print("*",end=" ")
##    print()


# # (iv) Full diamond

# for i in range (7):
#     for j in range (6-i):
#         print(" ",end=" ")
#     for k in range (2*i+1):
#         print("*",end=" ")
#     print()
# for l in range(5,-1,-1):
#     for m in range (6-l):
#         print(" ",end = " ")
#     for n in range(2*l+1):
#         print("*",end=" ")
#     print()

    
