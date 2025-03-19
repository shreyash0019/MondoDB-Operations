# MongoDB Operations Sample

This repository contains a sample script to perform basic MongoDB operations (CRUD) on a collection using random data. The script is written in Python and uses the `pymongo` package to interact with MongoDB.

## Prerequisites

- MongoDB installed and running on your local machine.
- Python installed on your local machine.
- `pymongo` package installed. You can install it using the following command:

```sh
pip install pymongo
```

## Files

- `mongo_operations.py`: The main script to perform MongoDB operations.
- `README.md`: This file containing instructions.

## Usage

1. Ensure MongoDB is running on your local machine.
2. Run the `mongo_operations.py` script using Python:

```sh
python mongo_operations.py
```

3. The script will perform the following operations:
   - Generate and insert 100 random documents into the `sample_collection`.
   - Read and print all documents from the collection.
   - Update documents where the age is less than 30 and add a `status` field with the value `young`.
   - Delete documents where the age is greater than 80.
   - Print the collection's state after each operation.

## License

This project is licensed under the MIT License.
