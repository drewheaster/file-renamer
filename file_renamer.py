import os
import time
import shutil
import glob
import requests
import smartsheet
import sys

profile = os.environ['USERPROFILE']

print('--L-COM File Renamer--')

file=input('Enter a part number to copy: ')+'.jpg'

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)


fast_photo_path_500=profile+'/OneDrive/Desktop/FastPhoto/L-COM/500x500/'+ file
fast_photo_path_250=profile+'/OneDrive/Desktop/FastPhoto/L-COM/250x250/'+ file
fast_photo_path_100=profile+'/OneDrive/Desktop/FastPhoto/L-COM/100x100/'+ file

fast_photo_paths = [ fast_photo_path_500, fast_photo_path_250, fast_photo_path_100 ]

endings = ['_500x500_View1.jpg', '_250x250_View1.jpg', '_100x100_View1.jpg']

images_500=profile+'/OneDrive/Desktop/Images/LARGE/'
images_250=profile+'/OneDrive/Desktop/Images/MEDIUM/'
images_100=profile+'/OneDrive/Desktop/Images/SMALL/'

new_contents=[]
new_contents_500=[]
new_contents_250=[]
new_contents_100=[]

for x in range(len(fast_photo_paths)):
    for i in range(len(contents)):
        new_contents.append(shutil.copy2(fast_photo_paths[x], fast_photo_paths[x].replace(file, contents[i] + '.jpg')))

for i in range(len(contents)):
    new_contents_500.append(fast_photo_path_500.replace(file,contents[i]+'.jpg'))
    new_contents_250.append(fast_photo_path_250.replace(file,contents[i]+'.jpg'))
    new_contents_100.append(fast_photo_path_100.replace(file,contents[i]+'.jpg'))


for i in range(len(fast_photo_paths)):
     shutil.copy(fast_photo_paths[i], fast_photo_paths[i].replace('.jpg', '') + endings[i])

for i in range(len(new_contents_500)):
    shutil.copy2(new_contents_500[i], new_contents_500[i].replace('.jpg', '_500x500_View1.jpg'))
    shutil.copy2(new_contents_250[i], new_contents_250[i].replace('.jpg', '_250x250_View1.jpg'))
    shutil.copy2(new_contents_100[i], new_contents_100[i].replace('.jpg', '_100x100_View1.jpg'))
    

extensions_500=(glob.glob(os.path.join(fast_photo_path_500.replace(file,''), '*_500x500_View1*'), recursive=True))
extensions_250=(glob.glob(os.path.join(fast_photo_path_250.replace(file,''), '*_250x250_View1*'), recursive=True))
extensions_100=(glob.glob(os.path.join(fast_photo_path_100.replace(file,''), '*_100x100_View1*'), recursive=True))


for i in range(len(extensions_500)):
    shutil.move(extensions_500[i], images_500)
    shutil.move(extensions_250[i], images_250)
    shutil.move(extensions_100[i], images_100)