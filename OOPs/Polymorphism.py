class Animals:
    def __init__(self,Animal="Some Animal"):
        self.Aname = Animal
    def Sound(self):
        return "Some Sound!!"
class Dog(Animals):
    def Sound(self):
        return "Brrrr Brrrrr WoooWWOwOWOW!!"
class Cat(Animals):
    def Sound(self):
        return"MEEEMeow meeeemeow!!"
class Birds(Animals):
    def Sound(self):
        return "KeeeeKuuuuKEeeeeeeeeekekekek!!"
Dog = Dog("Jack")
Cat = Cat("Pinky")
Birds = Birds("Kuttu")
AnimalSound = [Dog,Cat,Birds]
for i in AnimalSound:
    print(f"{i.Aname} Says {i.Sound()}")



