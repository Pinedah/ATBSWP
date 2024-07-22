#! python3
# Permanently Deleting Files and Folders

"""
    os.unlik(path)      - delete the file at path
    os.rmdir(path)      - delete the folder at path (folder must be empty)
    shutil.rmtree(path) - remove the folder at path and all files and folder it contains 
"""

import os, shutil

dir = '1_shutil-copy'

if os.path.exists(dir):
    for filename in os.listdir(dir):
        if filename.endswith('.txt'):
            os.unlink(dir + '\\' + filename)
            print(filename)
    print('\n deleted...')

if os.path.exists(dir) and not os.listdir(dir) == []:
    for filename in os.listdir(dir):
        os.unlink(dir + '\\' + filename)
    os.rmdir(dir)


dir2 = '1_shutil'
shutil.rmtree(dir2) # removes everything lmao!