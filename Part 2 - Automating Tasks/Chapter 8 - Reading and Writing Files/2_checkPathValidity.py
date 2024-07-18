#! python3
# Checking Path Validity

import os


print()
print(os.path.exists('C:\\Windows')) # T
print(os.path.exists('C:\\some_made_up_folder')) # F

print()
print(os.path.isdir('C:\\Windows\\System32')) # T
print(os.path.isdir('C:\\Users\\Dell Latitude\\Documents\\CECyT 3\\CECyT Calificaciones.xlsx')) # F

print()
print(os.path.isfile('C:\\Users\\Dell Latitude\\Documents\\CECyT 3\\CECyT Calificaciones.xlsx')) # T
print(os.path.isfile('C:\\Windows\\System32')) # F

