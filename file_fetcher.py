import os
import time
import shutil
import glob
import requests
import smartsheet
import inquirer

### Nate's funny business ###
class Brand():
    Brand_Selection = ''
    Image_Size_1 = ''
    Image_Size_2 = ''
    Image_Size_3 = ''

###                       ###

# set brand

brand_list = [
    'L-COM', 'Fairview', 'Pasternack', 'ShowMeCables', 'Transtector'
]

def initialPrompt(brand_list):
    brand = inquirer.prompt([
    inquirer.List(
        'Brand_Selection',
        message='Select the brand:',
        choices=brand_list,
    ),
    ])
    return brand['Brand_Selection']


brand_choice = initialPrompt(brand_list)
# Locator #

# Set name = user input
start = input('Part number: ')
og_pn = start.strip() + '.jpg'

# Set path = brand selected through inquire
path = '/Users/drewh/OneDrive/Desktop/File Copier Script/' + brand_choice

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
new_pn = '/'+ og_pn.replace('.jpg', '')
new_name = path + new_pn + '.jpg'

# os.rename(file_path, new_name)

# print('File name has been changed to ' + new_pn + '.')

# print('Copying files...')

time.sleep(2)

#------------------------------------------------------------#
# Copier #

endings = ['_500x500_View1.jpg', '_250x250_View1.jpg', '_100x100_View1.jpg']
pe_endings = ['_500x334_View1.jpg', '_250x167_View1.jpg', '_100x67_View1.jpg']
# src = new_name

def copier(new_name, new_pn, endings, pe_endings):
    if brand_choice == 'Pasternack':
        for extension in pe_endings:
            src = new_name
            dst = path + new_pn + extension
            shutil.copy(src, dst)
    else:
        for extension in endings:
            src = new_name
            dst = path + new_pn + extension
            shutil.copy(src, dst)

copier(new_name, new_pn, endings, pe_endings)

print('File copies have been made.')
print('Extensions have been added.')

time.sleep(1)

print('Relocating files...')

time.sleep(3)

#------------------------------------------------------------#
# File Mover #

source = path

if brand_choice == 'Pasternack':
    my_paths = {
        glob.glob(os.path.join(source, '*_500x334_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Documents/FastPhoto/'+ brand_choice +'/500x334',
        glob.glob(os.path.join(source, '*_250x167_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Documents/FastPhoto/'+ brand_choice +'/250x167', 
        glob.glob(os.path.join(source, '*_100x67_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Documents/FastPhoto/'+ brand_choice +'/100x67'
    }
else:
    my_paths = {
        glob.glob(os.path.join(source, '*_500x500_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Documents/FastPhoto/'+ brand_choice +'/500x500',
        glob.glob(os.path.join(source, '*_250x250_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Documents/FastPhoto/'+ brand_choice +'/250x250', 
        glob.glob(os.path.join(source, '*_100x100_View1*'), recursive=True)[0]: '/Users/drewh/OneDrive/Documents/FastPhoto/'+ brand_choice +'/100x100'
    }

def file_mover(my_paths):
    for file in my_paths:
        dst_path = os.path.join(my_paths[file], os.path.basename(file))
        shutil.move(file, dst_path)

file_mover(my_paths)

print('Files have been moved :)')