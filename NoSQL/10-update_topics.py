#!/usr/bin/env python3
"""Update a document in Python"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """Update a document in a collection"""
    mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})