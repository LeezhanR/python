from pymongo import MongoClient
connect=MongoClient('mongodb://localhost:27017/')
db=connect['CARS']
types=db['TYPES']
BRANDS=[{"Volkswagen":{"Audi":"R8","Bentley":"Continental GT","Prosche":"911 GT3RS"}},
        {"TATA":{"Tata Motors":"Punch","Jaguar":"F-Pace","Land Rover":"Defender"}}]
types.insert_many(BRANDS)
Finding=types.find_one({"TATA.Tata Motors":{"$exists":True}},{"TATA.Tata Motors":1,"_id":0})
print(Finding)
types.update_one({"TATA.Tata Motors":{"$exists":True}},{"$set":{"TATA.Tata Motors":"Nexon"}})
updated_finding = types.find_one({"TATA.Tata Motors": {"$exists": True}}, {"TATA.Tata Motors": 1, "_id": 0})
print(f"After Update: {updated_finding}")