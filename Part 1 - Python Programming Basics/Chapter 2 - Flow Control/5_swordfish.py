
# example for CONTINUE in a loop

while True:
    print("\nWho are you?")
    name = input()
    if name == 'panke':
        print("\nHi, " + name + "!")
    else:
        print("Who?")
        continue

    print("What is the password? (its a fish)")

    password = input()
    if password == 'swordfish':
        break

print("Access granted!!!")