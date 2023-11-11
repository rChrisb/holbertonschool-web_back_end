#!/usr/bin/env python3
""" no sql """


from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.logs
collection = db.nginx

logs_count = collection.count_documents({})

print(logs_count, "logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    method_count = collection.count_documents({"method": method})
    print(f"\t{method}: {method_count}")

status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(status_count)
