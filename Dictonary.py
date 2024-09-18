# a = {"Name": "Leezhan ","Place": "Pondicherry", "Age" : 18 , "Course" : "Data Analyst"}
# ##print(a)
# ##print(type(a))
# ##print()
# ##print(a["Name"])
# ##print()
# ##print(a["Place"])
# ##print()
# ##print(a["Age"])
# ##print()
# ##print(a["Course"])
# ##print()
# ### Changing values
# ##a["Name"]="Samuel"
# ##print(a)
# ##print()
# ##a["Name"] = "Leezhan "
# ##print(a)
# ##print()
# # Methodes

# # 1 . keys()
# print(a.keys())
# print()
# # 2 . values()
# print(a.values())
# print()
# # 3 . items()
# print(a.items())
# print()
# # 4 . get()
# print(a.get("Name"))
# print()
# # Loops
# # 1 . for loop
# # (i) Access keys
# fint(ior i in a:
#     pr)#Default returns keys
# print("-"*10)
# # (ii) Access values
# for i in a:
#     print(a[i])
# print("-"*10)
# # 2 . while loop
# # (i) Access values
# b = len(a)
# i = 0
# while i <= b:
#     print(a.values())
#     i+=1
# print("-"*10)
# # (ii) Access keys
# b = len(a)
# i = 0
# while i <= b:
#     print(a.keys())
#     i+=1
# print("-"*10)
# dictionary in an dictionary
d = {"Roll.No:1":{"Name":"Leezhan . R","Age":18,"Height":160,"Weight":50},
     "Roll.No:2":{"Name":"Samuel","Age":18,"Height":170,"Weight":60}
     }
print(d)
#Accessing an element in an dictionary
print(d["Roll.No:1"])
print(d["Roll.No:2"])
#Accessing an Dictionary inside an dictionary
print(d["Roll.No:1"]["Name"])
print(d["Roll.No:2"]["Name"])
# Changing An element in an dictionary
d1 = {"Name":"Leezhan . R","Age":18,"Height":160,"Weight":50}
d2 = d1.copy()
d2.setdefault("Name","Lee")
print(d2)
d2.update({"Name":"Lee"})
print(d2)
a = d.copy()
print(a)














