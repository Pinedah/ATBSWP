"""

    Conditions:
        if
        else
        elif

    Blcks of code:
        uses identation

"""

# name = 'panke'
# password = 1234

name = input()
password = int(input())

if(name == 'panke'):
    print("hello " + name)

if(password == 1234):
    print("access granted, " + name + ", use another fkn password, bro, wtf is " + str(password))
elif(password == 12345):
    print("really?")
else:
    print("wrong password :)")