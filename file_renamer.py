import os
import time
import shutil
import glob
import requests
import smartsheet
import inquirer


#tell the user what brand they are working with
print('--L-COM File Renamer--')
time.sleep(2)
gid=input('What is the GID? ')

file=input('Enter a part number to copy: ')+'.jpg'

fast_photo_path_500='C:/Users/drewh/OneDrive/Desktop/FastPhoto/L-COM/500x500/'+file
fast_photo_path_250='C:/Users/drewh/OneDrive/Desktop/FastPhoto/L-COM/250x250/'+file
fast_photo_path_100='C:/Users/drewh/OneDrive/Desktop/FastPhoto/L-COM/100x100/'+file

images_500='C:/Users/drewh/OneDrive/Desktop/Images/LARGE/'
images_250='C:/Users/drewh/OneDrive/Desktop/Images/MEDIUM/'
images_100='C:/Users/drewh/OneDrive/Desktop/Images/SMALL/'

shutil.copy(fast_photo_path_500, fast_photo_path_500.replace('.jpg', '') + '_500x500_View1.jpg')
shutil.copy(fast_photo_path_250, fast_photo_path_250.replace('.jpg', '') + '_250x250_View1.jpg')
shutil.copy(fast_photo_path_100, fast_photo_path_100.replace('.jpg', '') + '_100x100_View1.jpg')

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