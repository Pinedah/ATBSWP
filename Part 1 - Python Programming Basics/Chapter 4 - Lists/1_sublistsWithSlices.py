
spam = ['cat', 'bat', 'rat', 'elephant']
#       0       1       2       3

"""
    when using slices:
        the value after the colon wont be included
        leaving any of the sides blank:
            left - print since the beginning
            righ - include all the way until the end
"""

print(f'spam:\t{spam}')

print(f'spam[0:2]:\t\t{spam[0:2]}')
print(f'spam[:2]:\t\t{spam[:2]}')

print(f'spam[1:-1]:\t\t{spam[1:-1]}')


print(f'spam[1:]:\t\t{spam[1:]}')
print(f'spam[1:4]:\t\t{spam[1:4]}')

print(f'spam[:]:\t\t{spam[:]}')