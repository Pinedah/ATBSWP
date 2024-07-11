#! python3
# Add commas every three digits 

def reverseString(string):
    return string[::-1] # sequence[star:stop:step]

def add_commas(number):
    reversed_num = reverseString(number) # reverse the number

    # parts = [expression for item in iterable]
    parts = [reversed_num[i:i+3] for i in range(0, len(reversed_num), 3)]
    print(parts)

    formatted_reversed_num = ','.join(parts) 
    return reverseString(formatted_reversed_num) 

while True:
    number = str(input())
    if number == '':
        break
    print(add_commas(number)+ '\n')
