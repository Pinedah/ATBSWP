
catNames = []

while True:
    print(f'Enter the name of cat {str(len(catNames) + 1)} (Or enter nothing to stop)')
    name = str(input())
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

print('The cat names are:')

for n in catNames:
    print('     ' + n)