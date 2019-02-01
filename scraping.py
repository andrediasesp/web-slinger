#!/usr/local/bin/python3
import re
from bs4 import BeautifulSoup
from downloading import download_webpage

def regex_scrap(url,search_regex):
    """
    Scrap specific urls using a search regex. Returns a list of all matches to process
    """
    html = download_webpage(url)
    content = re.findall(search_regex,html)
    return content

def soup_html(html):
    """
    Create a soup object from a html doc
    """
    soup = BeautifulSoup(html,'html5lib')
    return soup

def search_soup(html):
    """
    Searching the Soup element for games in promotion state. Inspect your target HTML to retrieve the elements.
    """
    content = html.find_all("div",{"class": "w-product"})
    # Writing to a file for easier analysis
    with open("soup_object.html",'w') as soup_file:
        soup_file.write(str(content))
    for element in content:
        game = element.find("img")['title']
        price = element.find("span", class_="w-currentPrice").text
        promotion = "{} ---- {}".format(game,price)
        print(promotion)

def main():
    #regex_scrap('https://www.worten.pt/promocoes?page=1&categoria=Gaming%20e%20Entretenimento',r'<td class="w2p_fw">(.*?)</td>')
    #games = regex_scrap('https://www.worten.pt/promocoes?page=1&categoria=Gaming%20e%20Entretenimento',r'''<div class="w-product qa-product__content.*data-category=["'](.*?)["'].*data-price=["'](.*?)["']''')
    page =  download_webpage('https://www.worten.pt/promocoes?page=1&categoria=Gaming%20e%20Entretenimento')
    soup = soup_html(page)
    search_soup(soup)

if __name__ == '__main__':
    main()