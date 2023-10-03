import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

# Retrieve the list from MongoDB
result = collection.find({})
data_list = [item for item in result]

# Do something with data_list
print(data_list)
