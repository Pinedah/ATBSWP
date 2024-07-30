#! python3
# Requests Module (needs to be installed)

import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt')")

print(type(res))
