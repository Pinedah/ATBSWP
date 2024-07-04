
"""
    Say you have a list value like this:
    spam = ['apples', 'bananas', 'tofu', 'cats']

     Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it

"""

def separate_list(list):
    if len(list) == 1:
        return str(list[0])

    string_list = ''

    for i in range(len(list)):
        if i == len(list) - 1:
            string_list += 'and ' + list[i]
        else:
            string_list += str(list[i]) + ', ' 

    return string_list


spam = ['apples', 'bananas', 'tofu', 11, 42, 'panke', 'cats']
eggs = ['a']

print(separate_list(spam))
print(separate_list(eggs))
