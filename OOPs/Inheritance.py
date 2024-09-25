# 1 . Single level inheritance

class Thatha:
    def __init__(self,ThathaName):
        self.Tname = ThathaName
class Dada(Thatha):
    def __init__(self,ThathaName,DadaName):
        self.Dname = DadaName
        Thatha.__init__(self,ThathaName)
    def __str__(self):
        return f"Yean peru {self.Dname} aparam yean appa peru {self.Tname}"

# peru = Dada("Aravinth","Aravinthan")
# print(peru)

# 2 . Multiple inheritance

class Paati:
    def __init__(self,PaatiName):
        self.PAname = PaatiName

class Pulla(Thatha,Paati):
    def __init__(self,ThathaName,PaatiName,PullaName):
        self.Pname = PullaName
        Thatha.__init__(self,ThathaName)
        Paati.__init__(self,PaatiName)
    def __str__(self):
        return f"Yean peru {self.Pname} yean Thatha peru {self.Tname} yean Paati peru {self.PAname}"

# Peru = Pulla("Thatha","Paati","Leezhan")
# print(Peru)

# 3 . Multi level inheritance

class Magan(Dada):
    def __init__(self,ThathaName,DadaName,MaganName):
        self.Mname = MaganName
        super().__init__(ThathaName,DadaName)
    def __str__(self):
        return f"na tha {self.Mname} ithu enga {self.Dname} apram ithu enga {self.Tname}"

# Generation = Magan("Thatha","Appa","Leezhan")
# print(Generation)


# 4 . Hierarchical inheritance

class pethi(Thatha):
    def __init__(self,ThathaName,PethiName):
        self.pname = PethiName
        super().__init__(ThathaName)
    def __str__(self):
        return f"yen peru {self.pname} ithu enga {self.Tname}"

class peran(Thatha):
    def __init__(self,ThathaName,PeranName):
        self.paname = PeranName
        super().__init__(ThathaName)
    def __str__(self):
        return f"yen peru {self.paname} ithu enga {self.Tname}"


GrandSon = peran("Thatha","Leezhan")
GrandDaughter = pethi("Thatha","Pastina")

print(GrandSon)
print()
print(GrandDaughter)

print("hello world")