import pymongo
import random
from bson.objectid import ObjectId

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

# Read data from the collection
def read_data():
    documents = collection.find()
    for doc in documents:
        print(doc)

# Update data in the collection
def update_data(query, new_values):
    result = collection.update_many(query, {"$set": new_values})
    print(f"Updated {result.modified_count} documents.")

# Delete data from the collection
def delete_data(query):
    result = collection.delete_many(query)
    print(f"Deleted {result.deleted_count} documents.")

# Main function to perform operations
def main():
    # Generate and insert random data
    data = generate_random_data(100)
    insert_data(data)

    # Read data
    print("\nReading data from the collection:")
    read_data()

    # Update data
    query = {"age": {"$lt": 30}}
    new_values = {"status": "young"}
    update_data(query, new_values)
    print("\nData after update:")
    read_data()

    # Delete data
    delete_query = {"age": {"$gt": 80}}
    delete_data(delete_query)
    print("\nData after deletion:")
    read_data()

if __name__ == "__main__":
    main()
