#!/usr/bin/env python3
""" no sql """

def update_topics(mongo_collection, name, topics):
    """update"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
