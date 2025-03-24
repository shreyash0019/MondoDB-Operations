import pymongo

# MongoDB connection string
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sample_db"]
collection = db["sample_collection"]

# Update data in the collection
def update_data(query, new_values):
    result = collection.update_many(query, {"$set": new_values})
    print(f"Updated {result.modified_count} documents.")

# Delete data from the collection
def delete_data(query):
    result = collection.delete_many(query)
    print(f"Deleted {result.deleted_count} documents.")

if __name__ == "__main__":
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
