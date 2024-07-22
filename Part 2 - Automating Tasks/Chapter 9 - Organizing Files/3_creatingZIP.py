#! python3
# Creating and Adding to ZIP Files

import zipfile 
newZip = zipfile.ZipFile('newZip.zip', 'w')
newZip.write('spam.txt', compress_type = zipfile.ZIP_DEFLATED)
newZip.close()