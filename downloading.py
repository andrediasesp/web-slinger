#!/usr/local/bin/python3
import requests

def download_webpage(url,user_agent='funnel_web',num_retries=3,charset='utf-8', proxy = None):
    """
    Downloads the HTML of a given URL using the Requests Framework
    """
    print('Downloading webpage from: ' + str(url) + '\n...')
    # Create a request object for url to get
    headers = {'User-Agent': user_agent}
    proxies = {'http': proxy}
    try:
        response = requests.get(url, headers=headers, proxies= proxies)
        response.raise_for_status()
        #print(type(response.headers))
        #print(response.headers)
        cs = response.encoding
        #print(cs)
        # If no charset specified in http header then decode using the default UTF-8
        if not cs:
            cs = charset
        print(response)
        html_page = response.text.encode(cs)
    except requests.exceptions.RequestException as e:
        print('Error while downloading page:', e.response.status_code, e.response.reason)
        html_page = None
        if num_retries > 0:
            if hasattr(e.response,'status_code') and 500 <= e.response.status_code < 600:
                # Retry downloading the page for 3 times for 5xx error codes (Server Side)
                return download_webpage(url,num_retries = num_retries - 1)
        #print(e.response.status_code)
    return html_page

def main():
    page = download_webpage('http://www.worten.pt')

if __name__ == '__main__':
    main()
