#! python3
# 6_downloadXdcd.py - Downloads every single XKCD Comic.

import request, os, bs4

url = "https://xkcd.com/"
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # TODO: Download the page

    # TODO: Find the URL of the comic image.

    # TODO: Download the image

    # TODO: Save the image to ./xkcd

    # TODO: Get the Prev butto's url

print("Done.")