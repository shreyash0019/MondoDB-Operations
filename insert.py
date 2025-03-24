import pymongo
import random

# MongoDB connection string
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sample_db"]
collection = db["sample_collection"]

# Generate random data
def generate_random_data(n):
    data = []
    for _ in range(n):
        document = {
            "name": f"Name_{random.randint(1, 1000)}",
            "age": random.randint(18, 90),
            "city": f"City_{random.randint(1, 100)}"
        }
        data.append(document)
    return data

# Insert random data into the collection
def insert_data(data):
    result = collection.insert_many(data)
    print(f"Inserted {len(result.inserted_ids)} documents.")

if __name__ == "__main__":
    data = generate_random_data(100)
    insert_data(data)
