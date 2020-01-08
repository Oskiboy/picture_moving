import os
import glob
import time as t
import shutil
import subprocess
from shutil import copyfile

MEM_STICK_PATH = "F:/DCIM/"
PICTURE_PATH = "D:/Users/Gro/Pictures"
CANNOT_FIND_CARD_ERROR = '#' * 40 +"""

Finner ikke minnekort!
Har du huska å koble den til?
Eventuelt prøv å bytte USB port.
Trykk enter for å avslutte.

""" + '#'*40

def translateMonth(month_number):
    """Translates month number to a Norwegian month name"""
    months = ["Januar", "Februar", "Mars", "April", "Mai",
              "Juni", "Juli", "August", "September", "Oktober",
              "November", "Desember" ]
    return months[month_number - 1]
 
def getFolderName():
    """Creates the correct folder path"""
    year = t.strftime("%Y")
    month = translateMonth(int(t.strftime("%m")))
    return os.path.join(year, month)

def createFolders(path_to_folder):
    """ Creates folder paths that are needed."""
    if not os.path.exists(path_to_folder):
        print("Lager nye mapper...")
        os.makedirs(path_to_folder)

def copyFiles(source, dest, formats=['jpg', 'JPG', 'AVI', 'avi']):
    """Copy all files from the source to the destination."""
    
    for f in formats:
        # Creates a GLOB of the source_path/**/*.${FORMAT}
        files = mem_stick_folders = glob.glob(
            os.path.join(source, "**", "*."+f)
        )
        for media_file in files:
            print("Kopierer fil: ", media_file)
            copyfile(
                media_file,
                os.path.join(dest, os.path.basename(media_file))
            )

def main():
    # First checks for the existence of the memory stick
    if not os.path.exists(MEM_STICK_PATH):
        print(CANNOT_FIND_CARD_ERROR)
        exit()

    # Creates a new path for pictures and then creates the correct folders.
    output_path = os.path.join(PICTURE_PATH, getFolderName())
    print(output_path)
    createFolders(output_path)
    
    # Retrieves a list of all folders in the memory stick.
    copyFiles(MEM_STICK_PATH, output_path)

    print("\nOverføring var vellyket!")
    
def update():
    """A crude way to update the local git repo."""
    currdir = os.getcwd()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    git = shutil.which('git')
    proc = subprocess.run([git, 'fetch'], stdout=subprocess.PIPE)
    proc = subprocess.run([git, 'pull'], stdout=subprocess.PIPE)
    print("Update result:", proc.stdout.decode('UTF-8'))
    os.chdir(currdir)


if __name__ == '__main__':
    print("#"*40 + "\nOppdaterer:")
    update()
    print()
    
    print("#"*40 + "\nKjører overføring:")
    main()
