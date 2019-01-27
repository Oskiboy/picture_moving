import os
import glob
import time as t
from shutil import copyfile

VERSION = (1, 1)    # Version number (MAJOR, MINOR)
mem_stick_path = "F:/DCIM/"
picture_path = "C:/Users/Gro/Pictures"

def translateMonth(month_number):
    """
     Translates month number to a Norwegian month name
    """
    months = ["Januar", "Februar", "Mars", "April", "Mai",
              "Juni", "Juli", "August", "September", "Oktober",
              "November", "Desember" ]
    return months[month_number - 1]
 
def getFolderName():
    """
     Creates the correct folder path
    """
    year = t.strftime("%Y")
    month = translateMonth(int(t.strftime("%m")))
    return "/" + year + "/" + month

def createFolders(path_to_folder):
    """
     Creates folder paths that are needed.
    """
    if not os.path.exists(path_to_folder):
        print("Lager nye mapper...")
        os.makedirs(path_to_folder)


def main():
    global mem_stick_path
    global picture_path

    # If the memory stick is not found the script cannot do anything.
    if not os.path.exists(mem_stick_path):
        print("Finner ikke minnepenn!")
        print("Har du huska å koble den til?")
        # This is to make the error readable in a windows terminal.        
        t.sleep(10)
        exit()
    else:
        os.chdir(mem_stick_path)
    
    """
    We want to store the pictures in a easy to understand folderstructure,
    basically Pictures/year/month.
    """
    picture_path += getFolderName()
    createFolders(picture_path)
    
    # Retrieves a list of all folders in the memory stick.
    mem_stick_folders = glob.glob("*")
    for d in mem_stick_folders:
        work_dir = mem_stick_path + "/" + d
        os.chdir(work_dir)
        print("Jobber i mappe:", work_dir)

        for p in glob.glob("*.jpg"):
            print("Kopierer bilde: ", p)
            copyfile(work_dir + "/" + p, picture_path + "/" + p)

main()
