import time as t

from picture_importer.importer import ImageImporter


def main():
    print("Hello!")
    t.sleep(2)
    try:
        imp = ImageImporter()
        imp.getPaths()
        print(imp.run())
    except:
        print("Could not create class.")
    t.sleep(5)

if __name__ == "__main__":
    main()
