#! python3
# Reading the Contents of Files


helloFile = open('C:\\Users\\Dell Latitude\\Documents\\GitHub\\ATBSWP\\Part 2 - Automating Tasks\\Chapter 8 - Reading and Writing Files\\3_files\\hi.txt')

helloContent = helloFile.read()
print(helloContent)

print()
sonnetFile = open('3_files\\sonnet29.txt')
sonnetContent = sonnetFile.readlines()
print(sonnetContent)