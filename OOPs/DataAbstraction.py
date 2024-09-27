from abc import ABC,abstractmethod
class Cars(ABC):
    def __init__(self,Brand,Model):
        self.Brand = Brand
        self.Model = Model
    @abstractmethod
    def Details(self):
        pass
    @abstractmethod
    def Engine(self):
        return "It has V4 engine"
    @abstractmethod
    def Sunroof(self):
        pass
    @abstractmethod
    def Capacity(self):
        return "It has seating capacity of 4-5 "
    @abstractmethod
    def DriveType(self):
        return "It is AWD"
    def Break(self):
        return "It stops the vehicle"
    def Accelerator(self):
        return "Speeds up .........!!!"
    def Steering(self):
        return "Used to control the direction"
    def Seatbelt(self):
        return "Used to hold us and to trigger the airbag"
class SUV(Cars):
    def Details(self):
        return f"This is an SUV type of car and it's Brand name is {self.Brand} and the model is {self.Model}"
    def Engine(self):
        return f"{self.Model} has generally V6 , V8 and inline-4 turbo"
    def Sunroof(self):
        return f"Generally it has sunroof "
    def Capacity(self):
        return f"{self.Model} has the seating capacity if 5-7 "
    def DriveType(self):
        return f"{self.Model} is mostly AWD and 4WD"
class Sedan(Cars):
    def Details(self):
        return f"This is an Senad type of car and it's Brand name is {self.Brand} and the model is {self.Model}"
    def Engine(self):
        return f"{self.Model} has generally V6 and inline-4 "
    def Sunroof(self):
        return f"Generally it has sunroof in mid and top range "
    def Capacity(self):
        return f"{self.Model} has the seating capacity if 4-5 "
    def DriveType(self):
        return f"{self.Model} is mostly FWD and RWD"
class Hatchback(Cars):
    def Details(self):
        return f"This is an Hatchback type of car and it's Brand name is {self.Brand} and the model is {self.Model}"
    def Engine(self):
        return f"{self.Model} has generally inline-4 and inline-3"
    def Sunroof(self):
        return f"Generally it does not has sunroof "
    def Capacity(self):
        return f"{self.Model} has the seating capacity if 4-5 "
    def DriveType(self):
        return f"{self.Model} is mostly FWD"
CarTypes = [SUV,Sedan,Hatchback]
for i in CarTypes:
    brand = input(f"Enter the brand name for {i.__name__} : ")
    model = input(f"Enter the model name for {brand} : ")

    car = i(brand,model)

    print("\n\ttCar Details :")
    print(car.Details())
    print(car.Engine())
    print(car.Sunroof())
    print(car.Capacity())
    print(car.DriveType())
    print("\n" + "-"*50 + "\n")