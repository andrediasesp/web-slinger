#!/usr/local/bin/python3
import re
from downloading import download_webpage

def regex_scrap(url,search_regex):
    """
    Scrap specific urls using a search regex. Returns a list of all matches to process
    """
    html = download_webpage(url)
    content = re.findall(search_regex,html)
    print(content)


def main():
    #regex_scrap('https://www.worten.pt/promocoes?page=1&categoria=Gaming%20e%20Entretenimento',r'<td class="w2p_fw">(.*?)</td>')
    regex_scrap('https://www.worten.pt/promocoes?page=1&categoria=Gaming%20e%20Entretenimento',r'<div class="w-product qa-product__content.*data-category="(.*?)"')

if __name__ == '__main__':
    main()
