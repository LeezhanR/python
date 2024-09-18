from pymongo import MongoClient
connection = MongoClient('mongodb://localhost:27017/')
db = connection["CRUD_Operations"]
collection = db["CRUD"]
Student_Data =  [
    {
      "_id":1,   
      "name": "Alice",
      "age": 30,
      "city": "London"
    },
    {
      "_id":2, 
      "name": "Bob",
      "age": 25,
      "city": "Paris"
    },
    {
      "_id":3,  
      "name": "Charlie",
      "age": 28,
      "city": "New York"
    },
    {
      "_id":4,  
      "name": "David",
      "age": 35,
      "city": "Berlin"
    },
    {
      "_id":5,  
      "name": "Eve",
      "age": 22,
      "city": "Tokyo"
    }
  ]
# 1 . Create 
def Creating():
  collection.insert_many(Student_Data)
# Creating()
# 2 . Reading 
def Reading(n):
  find=collection.find().limit(n)
  for i in find:
    print(i)
# Reading()
# 3 . Update 
def Update():
  collection.update_one({"name":"Bob"},{"$set":{"name":"Samuel"}})
# Update()
# Reading(2)
# 4 . Drop or Deleting 
def Drop(a):
  collection.delete_one(a)
# 1 - C
# Creating()
# 2 - R 
Reading(3)
# 3 - U
Update()
Reading(5)
# 4 - D
Drop({"age":30})
Reading(5)
