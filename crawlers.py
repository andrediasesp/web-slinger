#!/usr/local/bin/python3
import re
import time
import downloading
import itertools
from urllib.parse import urljoin
import scraping

def crawl_website_sitemap(url):
    """ Crawls websites sitemap. Doesn't cover sitemaps gz files """
    # Crawl a given website's sitemap
    sitemap = downloading.download_webpage(url)
    # Extract all links from a given sitemap - lazy mode
    site_links = re.findall(r'<loc>(.*?)</loc>',sitemap)
    for link in site_links:
        html_page = downloading.download_webpage(link)
        time.sleep(2)

def crawl_website_ID(url, max_errors = 3):
    """ Crawler based on database ID Links. Maximum 3 consecutive
        non-existing webpages to break execution. Calls scraping method to
        retrieve info from website pages.
        Returns a List of all the information found across all pages scrapped
    """
    # Creating a seen set to prevent website redirection to last page when surpassing page id
    seen = set()
    collect = []
    # Crawl all website ids
    for id in itertools.count(start=1):
    # Testing only for the first four webpages
    #for id in range(1,5):
        page_id = '{}{}'.format(url,id)
        if page_id not in seen:
            seen.add(page_id)
            html_page = downloading.download_webpage(page_id)
            # 2 seconds delay between requests, don't want to overload the server
            time.sleep(2)
            if html_page is None:
                num_errors += 1
                if num_errors == max_errors:
                    break
            else:
                num_errors = 0
                soup = scraping.soup_html(html_page)
                add_collect = scraping.search_soup(soup)
                #print(add_collect)
    collect.extend(add_collect)
    return collect


def main():
    crawl_website_ID('https://www.worten.pt/promocoes?categoria=Gaming%20e%20Entretenimento&tipologia=Jogos%20PS4&page=')

if __name__ == '__main__':
    main()
