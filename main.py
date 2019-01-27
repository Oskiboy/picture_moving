import os
import glob
import time as t
from shutil import copyfile
import picture_importer.importer as pim

def main():
    print("Hello!")
    t.sleep(2)
    try:
        imp = im.ImageImporter()
        imp.getPaths()
        print(imp.run())
    except:
        print("Could not create class.")
    t.sleep(5)

if __name__ == "__main__":
    main()

