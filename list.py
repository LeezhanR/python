l = [1,2,3,"a","b","c"] #mutable - changable

#it can be altered after it has been created.
##print(l)

#Ordered - indexed
##print(l[0])
##print(l[-1])#indexing
##print(l[:2])#slicing


#Changable

l[2] = 5
print(l)

#allow duplicated
l2 = [1,2,3,3,3,4,4,4,"a","a","b","b","c"]
print(l2)


#length of a list
print(len(l2))

#allows multiple datatypes to store
l3 = [1,2.2,"a",True,[1,2,3],(1,2,3)]#int, float, str, list, bool, tuple
print(l3)

#type

print(type(l3))

#list constructor
print(list((1,2,3,4,5)))

#access its items
print(l3[2])
print(l3[-2])

#access multiple elements
print(l3[:5])
print(l3[-5:])#last three items

#list in if statement
#check if item exists

l = [1, 2, 5, 'a', 'b', 'c']

#1
if "a" in l:
    print(True)
else:
    print(False)
#2
print("a" in l)

#1 & 2 returns the same output

#use list in loop

for i in l3:
    print(i)

#change a range of items in the list

l[:3] = [8,9,10]
print(l)

#if we assign less or more item, it will remove the item from the list for that particular index

#list methods:-

#1. insert - to insert an item in the existing list
l.insert(-1,"d") #(index, value)
print(l)


#2.append - to add an item at the end
l.append("alan")
print(l)

#3.extend - add the items from another list to the list
e = [5,6,7]
l.extend(e)
print(l)

l.extend(("tuple1","tuple2"))
print(l)

#4. remove - removes an item

l.remove("tuple2")
l.remove("alan")

#5. pop - remove specified index

l.pop(0)
print(l)

l.pop() #default - removes the last item
print(l)

#6. del - keyword - removes the list or specified index

##del l[0] #first item deleted
##print(l)

##del l #completely deleted the list
##print(l)

#7. clear - returns an empty list

##l.clear()
print(l)


#iterate through the index using for loop

for i in range(len(l)):
    print("index:",i)
    print("value",l[i])
    print()

#iterate through the index using while loop
print("while loop","-"*30,"\n")

i = 0
while i < len(l):
    print("index:",i, "value:",l[i])
    print()
    i+=1

#list comprehension
#Basic syntax: [newlist = [expression for item in iterable if condition == True]
    
result = [i for i in range(1,11)]
print(result)

even = [i for i in range(1,11) if i%2==0]
print("even numbers:",even)

#in case of multiple conditions or while using else

evenOdd = ["even" if i%2==0 else "odd" for i in range(1,11)]
print(evenOdd)


s = "hello"
print([i for i in s])
#or
print(list(s))

#sort - sorts the list items
l = [9,8,7,6,5,4,3,2,1]
print(f"Before sorting : {l}")
l.sort()#sorts in ascending order (default)
print(f"After sorting : {l}")

#sort in descending order
l.sort(reverse = True) #default -> reverse = False
print(f"after applying <reverse = True> : {l}")


s = [chr(i) for i in range(122,96,-1)]
print(f"before sort : {s}")

print()
##b = []
##for i in range(97,122):
##    b.append(chr(i))
##print(b)

s.sort()
print(f"after sort : {s}")

#copy - will copy the list and can be stored in another variable



a = s.copy()
print(f"s : {s}")
print()
print(f"a : {a}")

#concatenate two list

print("list 1 + list 2")
print("result :",l+s)
