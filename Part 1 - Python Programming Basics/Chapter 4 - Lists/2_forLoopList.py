
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

# in this one, i, is acting just like an index number, you could process it arithmetically, for example
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


for j in [3,4,5,6]:
    print(j)

pan = ['dona', 'concha', 'panke']
# here, p, is an list element, you couldnt do math with it
for p in pan:
    print(p)
    # print(p + 1) TypeError
    # print(int(p)) Value Error

print()
print()

# in this one, we print the list backwards
for i in range(len(supplies) - 1, -1, -1):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])