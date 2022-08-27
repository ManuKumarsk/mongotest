import pymongo

client = pymongo.MongoClient("mongodb+srv://manukumar:msk_1995@manukumar.otzciul.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"manukumar",
    "email":"manukumarsk95@gmail.com",
    "surname":"kumar"
}

db1=client['mongotest']
collection=db1['test']
collection.insert_one(d)