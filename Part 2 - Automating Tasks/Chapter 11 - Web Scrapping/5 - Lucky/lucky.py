#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, logging, pprint

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')

print('Googling...') # display text while downloading the Google page

logging.info(sys.argv)
logging.info('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#logging.info(res.text)

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# TODO: Open a browser tab for each result.

# linkElems = soup.select('.r a')
linkElems = soup.select('.egMi0') # class = "yuRUbf"
logging.info(pprint.pformat(linkElems))

aSoup = bs4.BeautifulSoup(str(linkElems), features='html.parser')

linkElems2 = aSoup.select('a') # class = "yuRUbf"

#logging.info(pprint.pformat(linkElems))
logging.info(pprint.pformat(linkElems2))
# logging.info(pprint.pformat(linkElems2[0].get('href')))


numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems2[i].get('href'))
    logging.info('http://google.com' + linkElems2[i].get('href'))
