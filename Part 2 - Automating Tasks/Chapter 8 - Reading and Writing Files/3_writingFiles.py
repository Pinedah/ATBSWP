#! python3
# Writing to Files

"""
    if you open the file with 'r' 
        you coulnd't write in it
    if you open the file with 'w'
        you will write, if the file has already content, it will be deleted
    if you open the file with 'a' (append)
        you will write, if the file has already content, it will keep the content and write at the end 
"""

baconFile = open('.\\3_files\\bacon.txt', 'w')
baconFile.write('Pankesito!\n')
baconFile.close()
# this will replace the content in bacon.txt for Pankesito!\n


baconFile = open('.\\3_files\\bacon.txt', 'a') # append mode
baconFile.write('Pankesito is not a bread.')
baconFile.close()


baconFile = open('.\\3_files\\bacon.txt') # read mode
content = baconFile.read()
baconFile.close()

print(content)

