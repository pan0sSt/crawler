#!/usr/bin/env python

import requests             # HTTP requests
import re                   # regural expressions
from urllib import parse    # split a URL string into its components, or combine URL components into a URL string


target_url   = "<INSERT WEBSITE HERE>"
target_links = []

# function that extracts all the links from a url get request
def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))

# function that collects and archives all the directories of a certain website
def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = parse.urljoin(url, link)  # if not complete link address, then make it

        if '#' in link:
            link = link.split('#')[0]

        if target_url in link and link not in target_links:  # keep only the specific website addresses
            target_links.append(link)
            print(link)
            try:
                crawl(link)  # recursive function to go deeper into a directory
            except UnicodeDecodeError:
                pass

crawl(target_url)
