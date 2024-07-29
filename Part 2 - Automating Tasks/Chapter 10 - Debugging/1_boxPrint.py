#! python3
#

def boxPrint(symbol, width, heigt):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string. :D')
    if width <= 2:
        raise Exception('Width must be greater than 2. :D')
    if heigt <= 2:
        raise Exception('Height must be greater that 2. :D')
    print(symbol * width)
    for i in range(heigt - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print(f'An exception happened, bruh: {err}')
        