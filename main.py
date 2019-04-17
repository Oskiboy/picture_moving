import os
import glob
import time as t
from shutil import copyfile
from subprocess import check_call as run
import subprocess

mem_stick_path = "F:/DCIM/"
picture_path = "C:/Users/Gro/Pictures"

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
    return "/" + year + "/" + month

def createFolders(path_to_folder):
    # Creates folder paths that are needed.
    if not os.path.exists(path_to_folder):
        print("Lager nye mapper...")
        os.makedirs(path_to_folder)

def resolve_path(executable):
    if os.path.sep in executable:
        raise ValueError("Invalid filename: %s" % executable)

    path = os.environ.get("PATH", "").split(os.pathsep)
    # PATHEXT tells us which extensions an executable may have
    path_exts = os.environ.get("PATHEXT", ".exe;.bat;.cmd").split(";")
    has_ext = os.path.splitext(executable)[1] in path_exts
    if not has_ext:
        exts = path_exts
    else:
        # Don't try to append any extensions
        exts = [""]

    for d in path:
        try:
            for ext in exts:
                exepath = os.path.join(d, executable + ext)
                if os.access(exepath, os.X_OK):
                    return exepath
        except OSError:
            pass

    return None

def main():
    global mem_stick_path
    global picture_path

    # First checks for the existence of the memory stick
    if not os.path.exists(mem_stick_path):
        print("Finner ikke minnepenn!")
        print("Har du huska å koble den til?")
        input()
        exit()
    else:
        os.chdir(mem_stick_path)
    
    # Creates a new path for pictures and then creates the correct folders.
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

def update():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    git = resolve_path("git")
    proc = subprocess.Popen('{0} pull'.format(git))
    print("Update result:", proc.communicate())


if __name__ == '__main__':
    update()
    main()
