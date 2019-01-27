import os
import glob
import time as t
from shutil import copyfile

class PictureMover():
    mem_stick_path = "F:/DCIM/"
    picture_path = "C:/Users/Gro/Pictures"
    
    def __init__(self, mem_stick_path = False, pic_path = False):
        if mem_stick_path:
            self.mem_stick_path = mem_stick_path
        if pic_path:
            self.picture_path = pic_path
        

    def translateMonth(self, month_number):
        """
        Translates month number to a Norwegian month name
        """
        months = ["Januar", "Februar", "Mars", "April", "Mai",
                "Juni", "Juli", "August", "September", "Oktober",
                "November", "Desember" ]
        return months[month_number - 1]


    def createFolders(self, path_to_folder):
        """
        Creates folder paths that are needed.
        """
        if not os.path.exists(path_to_folder):
            print("Lager nye mapper...")
            os.makedirs(path_to_folder)


    def getFolderName(self):
        """
        Creates the correct folder path
        """
        year = t.strftime("%Y")
        month = self.translateMonth(int(t.strftime("%m")))
        return "/" + year + "/" + month

    def run(self):
        if not os.path.exists(self.mem_stick_path):
            print("Finner ikke minnepenn!")
            print("Har du huska å koble den til?")
            # This is to make the error readable in a windows terminal.        
            t.sleep(10)
            return -1
        else:
            os.chdir(self.mem_stick_path)
        
        """
        We want to store the pictures in a easy to understand folderstructure,
        basically Pictures/year/month.
        """
        self.picture_path += self.getFolderName()
        self.createFolders(self.picture_path)
        
        # Retrieves a list of all folders in the memory stick.
        mem_stick_folders = glob.glob("*")
        for d in mem_stick_folders:
            work_dir = self.mem_stick_path + "/" + d
            os.chdir(work_dir)
            print("Jobber i mappe:", work_dir)

            for p in glob.glob("*.jpg"):
                print("Kopierer bilde: ", p)
                copyfile(work_dir + "/" + p, self.picture_path + "/" + p)

        return 0
