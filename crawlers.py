#!/usr/local/bin/python3
import re
import time
import downloading
import itertools
from urllib.parse import urljoin
import scraping

def crawl_website_sitemap(url):
    """ Crawling websites sitemap."""
    # Crawl a given website's sitemap
    sitemap = downloading.download_webpage(url)
    # Extract all links from a given sitemap - lazy mode
    site_links = re.findall(r'<loc>(.*?)</loc>',sitemap)
    for link in site_links:
        html_page = downloading.download_webpage(link)
        time.sleep(3)
        #print(html_page)

def crawl_website_ID(url, max_errors = 3):
    """ Crawler based on database ID Links. Maximum 3 consecutive non-existing webpages to break execution """
    seen = set(url)
    info = {}
    for id in itertools.count(1):
        page_id = '{}{}'.format(url,id)
        if page_id not in seen:
            seen.add(page_id)
            html_page = downloading.download_webpage(page_id)
            # 3 seconds delay between request, don't want to overload the server
            time.sleep(3)
            if html_page is None:
                num_errors += 1
                if num_errors == max_errors:
                    break
            else:
                num_errors = 0

def main():
    #crawl_website_sitemap('http://example.webscraping.com/sitemap.xml')
    crawl_website_ID('https://www.worten.pt/promocoes?categoria=Gaming%20e%20Entretenimento&tipologia=Jogos%20PS4&page=')

if __name__ == '__main__':
    main()
