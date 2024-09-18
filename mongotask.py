from pymongo import MongoClient
connection=MongoClient('mongodb://localhost:27017/')
data_base=connection['GroceryShop']
collection=data_base['items']
Grocery_items=[{"Dairy Products":{}},
               {"Grains":{}},
               {"Bread items":{}}]
collection.insert_many(Grocery_items)
while True :
    Items=int(input('''Hi Sir Welcome! What do you want?\n 
    1 . Dairy Products
    2 . Grains
    3 . Bread items
    4 . Finished Shopping
    Enter a number to select :'''))
    if Items==4:
        print("Thankyou for shopping !\n")
        break
    match Items:
        case 1:
            Product=input('''You have selected Dairy products and what do you want in it : ''')
            Quantity=input(f'How many {Product} did you want ? ')
            collection.update_one({},{"$set":{f"Dairy Products.{Product}":Quantity}})
        case 2:
            Product=input('''You have selected Grains and what do you want in it : ''')
            Quantity=input(f'How many {Product} did you want ? ')
            collection.update_one({},{"$set":{f"Grains.{Product}":Quantity}})
        case 3:
            Product=input('''You have selected Bread Items and what do you want in it : ''')
            Quantity=input(f'How many {Product} did you want ? ')
            collection.update_one({},{"$set":{f"Bread items.{Product}":Quantity}})
Selected_items = collection.find_one({},{"_id":0})
print(f"\nThe Selected grocery items are: \n{Selected_items}")
