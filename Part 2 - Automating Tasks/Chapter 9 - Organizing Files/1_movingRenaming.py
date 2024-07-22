#! python3
# Moving and Renaming files and folders

# shutil.move(sourcer, destination)

import shutil

shutil.move('spam2.txt', '1_shutil-copy')
print('\nFile moved!')