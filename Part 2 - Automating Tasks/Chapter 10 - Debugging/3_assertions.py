#! python3
# Assertions 

# the variable is defined as 'open'
podBayDoorStatus = 'open'

# assert define the conditions as 'open', and the AssertionError as 'The pod...'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# the var is open, so its TRUE, and the program can continue

# the variable now is overwritten as 'I'm sorry ...'
podBayDoorStatus = "I'm sorry, Dave. I'm afraid I can't do that."


# Assert evaluates again 'open', as long as its false, now displays the AssertionError
assert podBayDoorStatus == 'open', "AssertionError changed to -> PANKE"
# change the error message for PANKE


print("The program does't get here")