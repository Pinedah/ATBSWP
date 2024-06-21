
# when  " + "  it used on two string values, it joins the strings as the string contatenation operator

print()
print('panke' + 'faxinaar')

# ////////////////////////////////////////////////
# if you try to use it with an string and an integer value, python wont know how to handle it

# print('panke ' + 11)

# The error message:
#  Can't convert 'int' object to str implicitly
#  means that Python thought you were trying to concatenate an integer to the string

# ////////////////////////////////////////////////
# As stupid as it sounds, if you try to use *, it'll work

# The * operator is used for multiplication when it operates on two integer or floating-point values. But when the * operator is used on one string value and one integer value, it becomes the: 
# string replication operator
# Enter a string multiplied by a number into the interactive shell to see this in action.

print()
print('panke' * 11)

# but, if you try to replicate two strings, then it'll die (finally)

