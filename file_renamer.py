import os
import time
import shutil
import glob
import requests
import smartsheet
import inquirer
import sys

#tell the user what brand they are working with
print('--L-COM File Renamer--')
# gid=input('What is the GID? ')

file=input('Enter a part number to copy: ')+'.jpg'

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

print(contents[0])

fast_photo_path_500='C:/Users/drewh/OneDrive/Desktop/FastPhoto/L-COM/500x500/'+ file
fast_photo_path_250='C:/Users/drewh/OneDrive/Desktop/FastPhoto/L-COM/250x250/'+ file
fast_photo_path_100='C:/Users/drewh/OneDrive/Desktop/FastPhoto/L-COM/100x100/'+ file

fast_photo_paths = [ fast_photo_path_500, fast_photo_path_250, fast_photo_path_100 ]

endings = ['_500x500_View1.jpg', '_250x250_View1.jpg', '_100x100_View1.jpg']

images_500='C:/Users/drewh/OneDrive/Desktop/Images/LARGE/'
images_250='C:/Users/drewh/OneDrive/Desktop/Images/MEDIUM/'
images_100='C:/Users/drewh/OneDrive/Desktop/Images/SMALL/'

for i in range(len(contents)):
    for x in range(len(fast_photo_paths)):
        shutil.copy2(fast_photo_paths[x], fast_photo_paths[x].replace(file, contents[i] + '.jpg'))

for i in range(len(fast_photo_paths)):
    shutil.copy(fast_photo_paths[i], fast_photo_paths[i].replace('.jpg', '') + endings[i])

my_paths = {
    glob.glob(os.path.join(fast_photo_path_500.replace(file,''), '*_500x500_View1*'), recursive=True)[0]: images_500,
    glob.glob(os.path.join(fast_photo_path_250.replace(file,''), '*_250x250_View1*'), recursive=True)[0]: images_250, 
    glob.glob(os.path.join(fast_photo_path_100.replace(file,''), '*_100x100_View1*'), recursive=True)[0]: images_100
}

def file_mover(my_paths):
    for i in my_paths:
        dst_path = os.path.join(my_paths[i], os.path.basename(i))
        shutil.move(i, dst_path)

file_mover(my_paths)