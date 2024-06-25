
name = input()
age = int(input())

if name == 'panke':
    print("hi, panke")
elif age < 12:
    print("you are not panke, kiddo")
elif age > 100: # here, we got a bug because of the wrong statements order
    print("unlike you, panke is not undead, inmortal vampire")
elif age > 2000:
    print("you are not panke, grannie")

