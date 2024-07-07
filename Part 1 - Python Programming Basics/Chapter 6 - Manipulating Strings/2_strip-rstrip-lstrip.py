
spam = '     Faxinaar Pineda Nava     '

print('\n' + '.' + spam + '.' + '\n')
print('.' + spam.strip() + '.')
print('.' + spam.rstrip() + '.')
print('.' + spam.lstrip() + '.')

print()
eggs = 'SpamSpamBaconSpamEggsSpamSpam'
print(eggs.strip('ampS'))
# doesn't matter the word 'Spam' is not in order -> ampS
# it will remove every a, m, p, S character