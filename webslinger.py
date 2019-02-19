#!/usr/local/bin/python3
import downloading
import crawlers
import scraping
import pymongo
from datetime import datetime


def run_slinger(url):

    # Make a MongoDB connection instance
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["crawling"]
    dblist = client.list_database_names()
    if "crawling" in dblist:
        print("The database exists.")
    # Crawl url to retrieve PS4 games in promotion and their price
    data = crawlers.crawl_website_ID(url)
    dict = {}
    for a,b in data:
        prom = {'game': a, 'price': b, 'insert_date': datetime.now()}
        result = database.promotions.insert_one(prom)

def main():
    run_slinger('https://www.worten.pt/promocoes?categoria=Gaming%20e%20Entretenimento&tipologia=Jogos%20PS4&page=')

if __name__ == '__main__':
    main()
