#! python3 
# Copying Files and Folders

# shutil Module (shell utilities)
import shutil, os

#os.chdir('Part 2 - Automating Tasks\\Chapter 9 - Organizing Files\\1_shutil')
path = shutil.copy('spam.txt', '1_shutil')
path2 = shutil.copy('spam.txt', '1_shutil\\eggs.txt')

print('\nThe new file is in: ' + path)
print('\nThe new file is in: ' + path2)


