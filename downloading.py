#!/usr/local/bin/python3
import requests

def download_webpage(url,user_agent='funnel_web',num_retries=3, proxy = None):
    """
    Downloads the HTML of a given URL using the Requests Framework
    """
    print('Downloading webpage from: ' + str(url) + '\n...')
    # Create a request object for url to get
    headers = {'User-Agent': user_agent}
    # Only taking care of HTTP proxies, if HTTPS proxies are required, add it into function param and in the following dict
    proxies = {'http': proxy}
    try:
        response = requests.get(url, headers=headers, proxies= proxies)
        response.raise_for_status()
        print(response.headers)
        html_page = response.text
    except requests.exceptions.RequestException as e:
        print('Error while downloading page:', e.response.status_code, e.response.reason)
        html_page = None
        if num_retries > 0 and 500 <= e.response.status_code < 600:
                # Retry downloading the page for 3 times for 5xx error codes (Server Side)
                return download_webpage(url,num_retries = num_retries - 1)
    return html_page
