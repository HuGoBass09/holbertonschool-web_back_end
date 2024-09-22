#!/usr/bin/env python3
"""MongoDB module for listing documents"""

import pymongo


def list_all(mongo_collection: pymongo) -> list:
    """A function to list all documents in a collection"""
    query = mongo_collection.find()
    if mongo_collection.count() == 0:
        return []

    return list(query)
