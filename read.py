import pymongo

# MongoDB connection string
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sample_db"]
collection = db["sample_collection"]

# Read data from the collection
def read_data():
    documents = collection.find()
    for doc in documents:
        print(doc)

if __name__ == "__main__":
    print("Reading data from the collection:")
    read_data()
