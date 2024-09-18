# 1 . Creating
def Create(name):
    try :
        with open(name,"x") as c:
            print(c)
    except Exception as e:
        print(f"{e} , Enter an non existing  file name")
# 2 . Writing
def Write(path,name):
    with open(path,"w") as w:
        w.write(name)
# 3 . Appending
def Append(path,name):
    with open(path,"a") as a:
        a.write(name)
# 4 . Reading
def Read(path):
    with open(path,"r") as r:
        print(r.read())


# Using all

Create("Cars.txt")
Write("Cars.txt","F1\nLamborgani\nTataNano\nFerrari")
Append("Cars.txt","\nAThar")
Read("Cars.txt")




