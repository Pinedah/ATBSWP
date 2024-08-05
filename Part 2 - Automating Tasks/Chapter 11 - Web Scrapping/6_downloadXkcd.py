#! python3
# 6_downloadXdcd.py - Downloads every single XKCD Comic.

import requests, os, bs4, logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.CRITICAL)

url = "https://xkcd.com/"
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # TODO: Download the page
    print(f"Downloading the page... {url}")
    res = requests.get(url)
    res.raise_for_status()

    logging.info(res.text)
    soup = bs4.BeautifulSoup(res.text)

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = comicElem[0].get('src')
        # TODO: Download the image
        print(f"Downloading the image... {comicUrl}")
        
        res = requests.get(comicUrl)
        res.raise_for_status()

    # TODO: Save the image to ./xkcd

    # TODO: Get the Prev butto's url

print("Done.")