import requests
from bs4 import BeautifulSoup
import json
import numpy as np
import time
import string    
import random 

"""Download and scrape a page on prnt.sc
Downloads and obtains the screenshot if found

:param id: id of the page to scrape
"""
def scrape(id):
    # Download the page content
    # Parse it with BeautifulSoup
    res = requests.get(f'https://prnt.sc/{id}', headers={"User-Agent":"Mozilla/5.0"})
    page = BeautifulSoup(res.text, 'html.parser')
    images = []
    for img in page.findAll('img'):
        images.append(img.get('src'))
        
    # Create our target string from the images list
    target = ""
    for i in images:
        target += i 
    
    # Check if "i.imgur.com" is in target
    # Download file if this is the case
    if "i.imgur.com" in target:
        start = target.index('i.imgur.com')
        end = target.index('.png',start)
        img_url = f'https://{target[start:end]}.png'

        # Get the filename and download it
        file_name = img_url.split('/')[-1]
        r = requests.get(img_url, allow_redirects=True)
        with open(filename, 'wb') as file:
            file.write(r.content);
        print("I found a image, and downloaded it!")
    else:
        print("....")

"""Generates a random page id
Lowercases all ids generated

:param length: Length of the id to generate
"""
def generateId(length):
    return ''.join(random.choices(string.ascii_lowercase, k = length))

"""Loop downloads multiple times
After a certain amount of attempts, increases the id length to attempt
"""
def __name__ == '__main__':
    for _ in range(200): 
        time.sleep(1.5)  
        scrape(generateId(4))

    for _ in range(600): 
        time.sleep(1.5)
        scrape(generateId(5))

    for _ in range(1000): 
        time.sleep(1.5)
        scrape(generateId(6))


