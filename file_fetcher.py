import os
import time
import shutil
import glob
import requests
import smartsheet


#Smartsheet API Token: 'RjRglnJVmdXGiCN3r6E1E1UarYq71aP2olLVK'


# Locator #

# Set name = user input
og_pn = 'example.txt'
# Set path = brand selected through inquire
path = '/Users/drewh/OneDrive/Desktop/File Copier Script'

def find(og_pn, path):
    for root, dirs, files in os.walk(path):
        if og_pn in files:
            return os.path.join(root, og_pn)
    return 'None found.'

      
file_path = find(og_pn, path)

print('File found in ' + file_path)

time.sleep(1)

print('Renaming files...')

time.sleep(2)

#------------------------------------------------------------#
# Renamer #
#write a function that queries smartsheet for PN's within a GID

#Set new_pn = function output of smartsheet part number query
new_pn = '/'+'newname'
new_name = path + new_pn + '.txt'

os.rename(file_path, new_name)

print('File name has been changed to ' + new_pn + '.')

print('Copying files...')

time.sleep(2)

#------------------------------------------------------------#
# Copier #

endings = ['_500x500_View1.txt', '_250x250_View1.txt', '_100x100_View1.txt']
# src = new_name

def copier(new_name, new_pn, endings):
    for extension in endings:
        src = new_name
        dst = path + new_pn + extension
        shutil.copy(src, dst)

copier(new_name, new_pn, endings)

print('File copies have been made.')
print('Extensions have been added.')

time.sleep(1)

print('Relocating files...')

time.sleep(3)

#------------------------------------------------------------#
# File Mover #

source = path

my_paths = {
    glob.glob(os.path.join(source, '*_500x500_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Desktop/500x500',
    glob.glob(os.path.join(source, '*_250x250_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Desktop/250x250', 
    glob.glob(os.path.join(source, '*_100x100_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Desktop/100x100'
}

def file_mover(my_paths):
    for file in my_paths:
        dst_path = os.path.join(my_paths[file], os.path.basename(file))
        shutil.move(file, dst_path)

file_mover(my_paths)

print('Files have been moved :)')