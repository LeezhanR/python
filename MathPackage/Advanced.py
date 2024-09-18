def factorial(a):
   if a==0 or a==1:
       return 1
   return a * factorial(a-1)
def prime(a):
    if a==1 or a==0:
        print(a,"is neither prime nor composite")    
    else:
        i = 2
        while i < a:
            if a%i==0:
                print(a," is not an prime number ")
                break
            i+=1
        print(a," is an prime number")