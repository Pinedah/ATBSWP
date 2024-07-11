#! python3
# Regex Version of Strip()
# Write a function that takes a string and does the same thing as the strip() string method

import re

def regexStrip(string, otherA):

    if string == '':
        return ''

    match otherA:
        case '':
            regex = re.compile(r'\S+')
            fa = regex.findall(str(string))
            if fa:
                return ' '.join(fa)
            else:
                return ''
            
        case _:
            regex = re.compile(f'[^{otherA}]')
            fa = regex.findall(str(string))
            if fa:
                return ''.join(fa)
            else:
                return string
    
print(regexStrip('xxxxxxPankesito Rexxxxxxxxxx', 'x'))
print(regexStrip('xxxxxxPankesito Rexxxxxxxxxx', ''))
print(regexStrip('               Pankesito Rex         ', 'e'))
print(regexStrip('       Fatima Nava Araujo     ', '') + '.')
print(regexStrip('* * * Fati*****ma N*ava *Araujo******', '*'))