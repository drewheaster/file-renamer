import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, Text
import os
import shutil
import glob

profile = os.environ['USERPROFILE']

def run_script(part_number, content_text):
    file = part_number + '.jpg'
    contents = content_text.split("\n")


    #set each starting path for files to be pulled from
    fast_photo_path_500=profile+'/OneDrive/Desktop/FastPhoto/L-COM/500x500/'+ file
    fast_photo_path_250=profile+'/OneDrive/Desktop/FastPhoto/L-COM/250x250/'+ file
    fast_photo_path_100=profile+'/OneDrive/Desktop/FastPhoto/L-COM/100x100/'+ file

    fast_photo_paths = [ fast_photo_path_500, fast_photo_path_250, fast_photo_path_100 ]


    #corresponding paths for where the final image files will end up
    images_500=profile+''
    images_250=profile+''
    images_100=profile+''

    new_contents_500 = [fast_photo_path_500]
    new_contents_250 = [fast_photo_path_250]
    new_contents_100 = [fast_photo_path_100]

    for x in range(len(fast_photo_paths)):
        for content in contents:
            if content:  # This checks to ensure content isn't empty
                new_file_path = fast_photo_paths[x].replace(file, content + '.jpg')
                shutil.copy2(fast_photo_paths[x], new_file_path)
                # Categorize the new files based on their resolution
                if x == 0:
                    new_contents_500.append(new_file_path)
                elif x == 1:
                    new_contents_250.append(new_file_path)
                else:
                    new_contents_100.append(new_file_path)

    # Use the newly copied files for renaming with endings
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
    # When done, show a success message
    messagebox.showinfo("Success", "Files have been renamed!")

def main():
    root = tk.Tk()
    root.title("File Renamer")
    root.iconbitmap('hedgehog.ico')
    # Create a label
    label = tk.Label(root, text="File Renamer")
    label.pack(pady=20)

    # Entry widget for the part number
    part_label = tk.Label(root, text="Enter a file-name to copy:")
    part_label.pack(pady=5)
    part_entry = tk.Entry(root, width=50)
    part_entry.pack(pady=5)

    # Text widget for content input
    content_label = tk.Label(root, text="Enter/Paste your content:")
    content_label.pack(pady=5)
    content_text = Text(root, height=10, width=50)
    content_text.pack(pady=5)

    # Button to run your script
    run_button = tk.Button(root, text="Run Script", command=lambda: run_script(part_entry.get(), content_text.get("1.0", tk.END)))
    run_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
