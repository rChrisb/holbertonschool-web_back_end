#!/usr/bin/env python3
""" no sql """

def insert_school(mongo_collection, **kwargs):
    """inserts doc into collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
