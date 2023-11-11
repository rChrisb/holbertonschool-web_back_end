#!/usr/bin/env python3
""" no sql """


from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.logs
collection = db.nginx

# Count the number of logs
logs_count = collection.count_documents({})

print(logs_count, "logs")

# Grouping methods and counting each one
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    method_count = collection.count_documents({"method": method})
    print(f"\t{method}: {method_count}")

# Checking logs with method=GET and path=/status
status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(status_count)
