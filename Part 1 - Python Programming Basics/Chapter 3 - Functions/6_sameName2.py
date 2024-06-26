
# 

def spam():
    global eggs
    eggs = '\neggs in spam with the global thing'

eggs = '\neggs in global, just like that'

spam()

print(eggs)
