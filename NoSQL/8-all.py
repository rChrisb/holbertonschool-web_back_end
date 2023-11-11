#!/usr/bin/env python3
""" no sql """

def list_all(mongo_collection):
    """lists all docs"""
    documents = list(mongo_collection.find())
    return documents if documents else []
