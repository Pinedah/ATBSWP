
# lists full of integers or strings (not both) can be sorted with sort()

numbers = [11, 1, -2, 0, 2, 0, 321, 33, -100]
print(f'\nnumbers:\t\t\t{numbers}')

numbers.sort()
print(f'numbers sorted:\t\t\t{numbers}')

numbers.sort(reverse = True)
print(f'numbers sorted in reverse:\t{numbers} \n')

# --------------------------------------------------

words = ['panke', 'fati', 'pato', 'citla', 'yoyo', 'kiara']
print(f'\nwords: {words}')

words.sort()
print(f'words sorted:{words}')

words.sort(reverse=True)
print(f'words sorted in reverse:{words}')

# --------------------------------------------------

wordsUpper = ['Panke', 'pankesito', 'Faxinaar', 'fati', 'Caramelo', 'citla', 'York', 'yoyo', 'Kitty', 'kiara']
print(f'\nwords w uppers:\n{wordsUpper}')

wordsUpper.sort()
print(f'words w uppers sorted (ASCII):\n{wordsUpper}')

wordsUpper.sort(reverse=True) # reverse = True makes the reverse sorting 
print(f'words w uppers sorted in reverse:\n{wordsUpper}')

wordsUpper.sort(key = str.lower)
print(f'words w uppers sorted all lowercase:\n{wordsUpper}') 
# this doesnt convert the strings in lowercase, its just for the sorting, but they still being Upper
