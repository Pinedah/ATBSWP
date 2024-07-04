
import copy

original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

# Modify the nested list in the original list
original_list[1] = 1000
original_list[2][0] = 'changed'

print("\nOriginal List:", original_list)
print(str(id(original_list)))

print("\nShallow Copy:", shallow_copy)       
print(str(id(shallow_copy)))

print("\nDeep Copy:", deep_copy)        
print(str(id(deep_copy)))

print('-------------------------------')

print("\nOriginal - nested id:")
print(str(id(original_list[2][0])))

print("\nCopy - nested id:")
print(str(id(shallow_copy[2][0])))

print("\nDeepCopy - nested id:")
print(str(id(deep_copy[2][0])))
