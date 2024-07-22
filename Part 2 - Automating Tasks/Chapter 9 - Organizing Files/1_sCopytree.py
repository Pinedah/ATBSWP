#! python3
# shutil.copytree() will copy an entire folder and every folder and file contained in it

import shutil, os

path = shutil.copytree('1_shutil', '1_shutil-copy')

print('Folder copied succesfully at: ' + path)
