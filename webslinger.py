#!/usr/local/bin/python3
import downloading
import crawlers
import scraping
import pymongo


def run_slinger():
    # Make a MongoDB connection instance
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["promotion_info"]
    print(client.list_database_names())
    if "promotion_info" in dblist:
        print("The database exists.")
