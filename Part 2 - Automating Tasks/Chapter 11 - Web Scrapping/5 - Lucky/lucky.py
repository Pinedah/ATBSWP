#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, logging, pprint

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.CRITICAL)

print('Googling...') # display text while downloading the Google page

logging.info(sys.argv)
logging.info('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Open a browser tab for each result.
searchResults = soup.select('.egMi0') # class = "egMi0" -> search divs that contain search links
logging.info(pprint.pformat(searchResults))

linkSoup = bs4.BeautifulSoup(str(searchResults), features='html.parser')
linkElems = linkSoup.select('a') # class = "yuRUbf" -> just links from the divs
logging.info(pprint.pformat(linkElems))

numOpen = min(5, len(linkElems)) # define the number of tabs to be open
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    logging.info('http://google.com' + linkElems[i].get('href'))
