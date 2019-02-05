#!/usr/local/bin/python3
import downloading
import crawlers
import scraping
import pymongo
import itertools



def run_slinger(url):
    """
    # Make a MongoDB connection instance
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["promotion_info"]
    print(client.list_database_names())
    if "promotion_info" in dblist:
        print("The database exists.")
    """
    data = crawlers.crawl_website_ID(url)
    id = 0
    dict = {}
    for a,b in data:
        dict[id] = {'game': a, 'price': b}
        id += 1

def main():
    run_slinger('https://www.worten.pt/promocoes?categoria=Gaming%20e%20Entretenimento&tipologia=Jogos%20PS4&page=')

if __name__ == '__main__':
    main()
