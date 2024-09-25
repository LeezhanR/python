class Bikes:
    def __init__(self,name,model,price,color,MaxSpeed):
        self.name=name
        self.model=model
        self.price=price
        self.color=color
        self.MaxSpeed=MaxSpeed
    def __str__(self):
        return f''' The name of your bike is {self.name} and the model name is {self.model} , 
the price of the bike is {self.price} and it is {self.color} color , 
The Maximum speed of {self.name} is {self.MaxSpeed} .'''


A = Bikes("Pulsar","Bajaj Pulsar RS200","1.73 lakh","black and red","140 km/h")
B = Bikes("TVS","TVS Apache RTR 160 4V","1.24 lakh","black","114 km/h")
C = Bikes("Royal Enfield","Royal Enfield Continental GT 650","3,45 lakh","silver","160 km/h")
D = Bikes("KTM","KTM Duke 200","1.99 lakh","red","142 km/h")
E = Bikes("Harley Davidson","Harley Davidson x440","2.39 lakh","black","160 km/h")

# a = input("Enter  any one A,B,C,D,E : ")
print(A)
print()
print(C)
# b = input("Enter the bike name :")
# c = input("Enter the details you want  like name , model , price , color , MaxSpeed : ")
print()
print(A.model)
print()
print(A.MaxSpeed)

