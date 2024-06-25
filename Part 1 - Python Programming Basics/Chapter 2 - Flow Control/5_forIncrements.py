
# for starting not with i = 0\

print('\nfor with k starting in 0 and ending in -5 with no step especification')
iterator0 = 1
for k in range(0, -5):
    print(f'i = {k} in the iteration = {iterator0}')
    iterator0 += 1
# python needs the second value to be positive

print('\nfor with k starting in 11 and ending in 17 with no step especification')
iterator = 1
for k in range(11, 17):
    print(f'i = {k} in the iteration = {iterator}')
    iterator += 1

    
print('\nfor with k starting in 10 and ending in 20 with 2 as the increment')
iterator2 = 1
for k in range(10, 20, 2):
    print(f'i = {k} in the iteration = {iterator2}')
    iterator2 += 1

print('\nfor with k starting in 0 and ending in -10 with -1 as the increment to be posible to count down')
iterator3 = 1
for k in range(0, -10, -1):
    print(f'i = {k} in the iteration = {iterator3}')
    iterator3 += 1

print('\nfor with k starting in 10 and ending in -6 with -1 as the increment to be posible to count down')
iterator3 = 1
for k in range(10, 5, -1):
    print(f'i = {k} in the iteration = {iterator3}')
    iterator3 += 1

    