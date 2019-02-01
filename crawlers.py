#!/usr/local/bin/python3
import re
import time
import downloading
import robot_parser
import itertools
from urllib.parse import urljoin

def crawl_website_sitemap(url):
    """ Crawling websites sitemap."""
    # Crawl a given website's sitemap
    sitemap = downloading.download_webpage(url)
    # Extract all links from a given sitemap - lazy mode
    site_links = re.findall(r'<loc>(.*?)</loc>',sitemap)
    for link in site_links:
        html_page = downloading.download_webpage(link)
        time.sleep(1)
        #print(html_page)

def crawl_website_ID(url, max_errors = 5):
    """ Crawler based on database ID Links. Maximum 5 consecutive non-existing webpages to break execution """
    for id in itertools.count(1):
        page_id = '{}{}'.format(url,id)
        html_page = downloading.download_webpage(page_id)
        time.sleep(1)
        if html_page is None:
            num_errors += 1
            if num_errors == max_errors:
                break
        else:
            num_errors = 0

def main():
    #crawl_website_sitemap('http://example.webscraping.com/sitemap.xml')
    crawl_website_ID('http://example.webscraping.com/places/default/view/-')

if __name__ == '__main__':
    main()
