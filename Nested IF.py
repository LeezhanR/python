### 1 . Loan eligiblity check 
##
##
##print('''Enter the required details to check the eligiblity for loan:
##1 . Age
##2 . Income
##3 . Credit Score''')
##A = int(input("1. Enter your Age :"))
##
##if A>=18:
##     print("Your Age criteria is satisifed")
##     B = int(input("2 . Enter your income :"))
##     if B>=40000:
##          print("Your Income criteria is satisifed")
##          C = int (input ("3 . Enter your credit score :"))
##          if C>=720:
##               print("Your Credit score is matched our criteria")
##               print("congrats! you are eligible for our loan")
##          else:
##               print("Sorry! you are not eligble because your credit score is less than 720 ")
##     else:
##          print("Sorry! you are not eligible because your income is less than 40000")
##else:
##     print("sorry! You are  not eligible because you are under 18")
##





### 2 . Checking positive or negative and even or odd
##
##
##A = int(input("Enter an number :"))
##
##match A :
##     case num if A>0 and A%2==0:
##          print("The number is positive and even")
##     
##     case num if A>0 and A%2!=0:
##          print("Thenumber is positive and odd")
##     case num if A<0 and A%2==0:
##          print("The number is negative and even ")
##     case num if A<0 and A%2!=0:
##          print("The number is negative and odd")
##     case _:
##          print("The number is zero")
##
# 3 . Determine weather(using match case)



##A = int (input("Enter an Weather (in celsius):"))
##
##
##match A:
##     case Weather if A>=30 and A<35:
##          print("The weather is hot ")
##     case Weather if A>=35:
##          print("The Weather is hot and advised to stay hydrated ")
##     case Weather if A<=15 and A>5:
##          print("The Weather is cold")
##     case Weather if A<=5:
##          print("The Weather is cold and adviced to wear warm clothing")
##     case Weather if A>15 and A<30:
##          print("The Weather is Moderate")


### 4 . Grade Checking
##
##
##
##
##A = int(input("Enter your mark :"))
##
##
##if A>=90 :
##     print("Your grade is A  ")
##
##else:
##     if A>=80 :
##          print("Your grade is B ")
##     else:
##          if A>=70 :
##               print("Your grade is C")
##          else:
##               if A>=60:
##                    print("Your grade is D")
##               else:
##                    print("Sorry ! You have failed and Your grade is F")
##










              
         
     

 






















