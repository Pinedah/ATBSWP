#! python3
# regex that matches a lastname

import re, pprint
print()

lastnameRegex = re.compile(r'[A-Z]\w+ Nakamoto')

fa = lastnameRegex.findall('Panke Nakamoto - Fati Nakamoto - yoyo Nakamoto - Citlaltzinnnnnnn Nakamoto - Pan Nakamoto - Kiara nakamoto - Nakamoto ')
print(fa)
print()

fa2 = lastnameRegex.findall('''
Panke Nakamoto
Fati Nakamoto 
yoyo Nakamoto              
Nakamoto
11 Nakamoto
Kiara Nakamoto
citlaaaaaaaa Nakamoto             
Someone nakamoto
CarameloNakamoto
Pan Nakamoto Pineda
Faxinaar Nakamoto Nava
''')
pprint.pprint(fa2)