
"""
When Gauss was a boy, a teacher wanted to give the class some busywork. The teacher told them to add up all the numbers from 0 to 100. Young Gauss came up with a clever trick to figure out the answer in a few seconds, but you can write a Python program with a for
loop to do this calculation for you
"""

total = 0

for number in range(101): # so it evaluates number 100 also
    total = total + number

print(total)