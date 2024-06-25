"""

==      equal to
!=      not equal to
<       less than
>       greater than
<=      less than or equal to
>=      greater than or equal to

"""

spam = "panke"

if(spam == 'panke'):
    print("spam == 'panke'")

if(spam == "panke"):
    print("spam == ''panke'' ")

# its posible to compare with ' ' or " "

if(len(spam) > 2):
    print("len(spam) > 2")

age = 18
if(age >= 18):
    print("go, fuck yourself")

age2 = 17
if(age2 != 0):
    print("!= 0")

string2 = 'notPanke'

if(spam != string2): # panke != notPanke
    print("wtf, you can compare two strings with !=")

if(spam != spam): # panke != panke | false, so don't go into the condition
    print("a")