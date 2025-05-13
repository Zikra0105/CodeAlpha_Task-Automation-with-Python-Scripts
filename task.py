import os
import shutil

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            ext_folder = os.path.join(folder_path, ext + "_files")

            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)

            shutil.move(file_path, os.path.join(ext_folder, filename))

# Change the path to your Downloads folder
organize_folder("D:/Zikra BSCIT/Random Folder")
