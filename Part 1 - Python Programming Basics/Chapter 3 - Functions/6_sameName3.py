
def spam():
	global eggs 
	eggs = '\nspam' # this is the global
	
def bacon():
	eggs = '\nbacon' # this is a local
	
def ham():
	print(eggs) # this is the global
	
eggs = 42
spam()
print(eggs)