#!/usr/bin/env python3
"""MongoDB module for listing documents"""

import pymongo


def list_all(mongo_collection) -> list:
    """A function to list all documents in a collection"""
    collections: list = []
    for doc in mongo_collection.find():
        collections.append(doc)
    return collections
