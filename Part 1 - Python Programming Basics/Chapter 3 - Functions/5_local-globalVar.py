def spam():
	eggs = 'spam local'
	print(eggs) # -> spam local

def bacon():
	eggs = 'bacon local'
	print(eggs) # -> bacon local
	spam()
	print(eggs) # -> bacon local
	
print()

eggs = 'global'
bacon()
print(eggs) # -> global