#!/usr/bin/env python3
""" no sql """

def schools_by_topic(mongo_collection, topic):
    """finds school thats match"""
    return list(mongo_collection.find({"topics": topic}))
