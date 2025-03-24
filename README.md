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

- `insert_data.py`: Script to generate and insert random data into the MongoDB collection.
- `read_data.py`: Script to read and print data from the MongoDB collection.
- `update_delete_data.py`: Script to update and delete data in the MongoDB collection.
- `README.md`: This file containing instructions.
- `LICENSE`: The MIT License file.

## Usage

1. Ensure MongoDB is running on your local machine.
2. Run the `insert_data.py` script to generate and insert random data:

```sh
python insert_data.py
```

3. Run the `read_data.py` script to read and print all documents from the collection:

```sh
python read_data.py
```

4. Run the `update_delete_data.py` script to update and delete documents in the collection:

```sh
python update_delete_data.py
```

5. The scripts will perform the following operations:
   - `insert_data.py`: Generate and insert 100 random documents into the `sample_collection`.
   - `read_data.py`: Read and print all documents from the collection.
   - `update_delete_data.py`: 
     - Update documents where the age is less than 30 and add a `status` field with the value `young`.
     - Delete documents where the age is greater than 80.
     - Print the collection's state after each operation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
