import os
import glob
import time as t
from shutil import copyfile

mem_stick_path = "F:/DCIM/"

picture_path = "C:/Users/Gro/Pictures"

def getFolderName():
    year = t.strftime("%Y")
    month = t.strftime("%B")
    return "/" + year + "/" + month

def createFolders(path_to_folder):
    if not os.path.exists(path_to_folder):
        print("Creating new folder")
        os.makedirs(path_to_folder)



def main():
    # First checks for the existence of the memory stick
    if not os.path.exists(mem_stick_path):
        print("Finner ikke minnepenn!")
        exit()
    else:
        os.chdir(mem_stick_path)
    
    # Creates a new path for pictures and then creates the correct folders.
    picture_path.append(getFolderName())
    createFolders(picture_path)
    
    # Retrieves a list of all folders in the memory stick.
    mem_stick_folders = glob.glob("*")
    for d in mem_stick_folders:
        work_dir = mem_stick_path + "/" + d
        os.chdir(work_dir)
        for p in glob.glob("*.jpg"):
            copyfile(work_dir + "/" + p, picture_path + "/" + p)
