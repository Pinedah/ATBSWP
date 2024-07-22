#! python3
# Rading ZIP Files

import zipfile, os
print()


#os.chdir()

exampleZip = zipfile.ZipFile('example.zip')

print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('cats/catnames.txt') # this could be any file inside the zipFile

print(spamInfo.file_size)
print(spamInfo.compress_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')

exampleZip.close()