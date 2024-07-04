
birthdays = {'Fati': 'Sep 1', 'Panke': 'Jan 5'}

while 1 == 1:
    print('\nEnter a name: (Blank to quit)')
    name = str(input())
    if name == '':
        break

    if name in birthdays:
        print('\n' + birthdays[name] + ' is the birthday of ' + name)
    else:
        print('\nI do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = str(input())
        birthdays[name] = bday
        print('Birthday database updated\n')