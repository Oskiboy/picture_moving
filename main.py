import os
import glob
import time as t
import shutil
import subprocess
from shutil import copyfile


mem_stick_path = "F:/DCIM/"
picture_path = "D:/Users/Gro/Pictures"

def translateMonth(month_number):
    # Translates month number to a Norwegian month name
    months = ["Januar", "Februar", "Mars", "April", "Mai",
              "Juni", "Juli", "August", "September", "Oktober",
              "November", "Desember" ]
    return months[month_number - 1]
 
def getFolderName():
    # Creates the correct folder path
    year = t.strftime("%Y")
    month = translateMonth(int(t.strftime("%m")))
    return os.path.join(year, month)

def createFolders(path_to_folder):
    # Creates folder paths that are needed.
    if not os.path.exists(path_to_folder):
        print("Lager nye mapper...")
        os.makedirs(path_to_folder)

def copyFiles(source, dest):
    mem_stick_folders = glob.glob(
        os.path.join(source, "*")
    )
    for d in mem_stick_folders:
        work_dir = os.path.join(source, d)
        print("Jobber i mappe:", work_dir)

        print("\nKopierer bilder...")
        for p in glob.glob(os.path.join(work_dir,"*.jpg")):
            print("Kopierer bilde: ", p)
            copyfile(
                p,
                os.path.join(dest, os.path.basename(p))
            )

        print("\nKopierer filmer...")
        for m in glob.glob(os.path.join(work_dir, '*.avi')):
            print("Kopierer film: ", m)
            copyfile(
                m,
                os.path.join(dest, os.path.basename(m))
            )


def main():
    global mem_stick_path
    global picture_path

    # First checks for the existence of the memory stick
    if not os.path.exists(mem_stick_path):
        print("Finner ikke minnepenn!")
        print("Har du huska å koble den til? Trykk enter for å avslutte.")
        input()
        exit()

    # Creates a new path for pictures and then creates the correct folders.
    picture_path = os.path.join(picture_path, getFolderName())
    createFolders(picture_path)
    
    # Retrieves a list of all folders in the memory stick.
    copyFiles(mem_stick_path, picture_path)

    print("\nOverføring var vellyket!")
    
def update():
    """A crude way to update the local git repo."""
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    git = shutil.which('git')
    proc = subprocess.run([git, 'fetch'], stdout=subprocess.PIPE)
    proc = subprocess.run([git, 'pull'], stdout=subprocess.PIPE)
    print("Update result:", proc.stdout)


if __name__ == '__main__':
    print("Oppdaterer:")
    update()
    print()
    
    print("Kjører overføring:")
    main()
