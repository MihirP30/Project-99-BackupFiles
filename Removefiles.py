from genericpath import isfile
import os
import shutil
import time

def removeFilesInCurrentFolder(path):
    days = 0
    seconds = 1

    if os.path.exists(path):
        for dir, folders, files in os.walk(path):
            # print("directory: " + str(dir))
            for file in files:
                print("deleting file: " + file)
                os.remove(dir + "/" + file)
            for folder in folders:
                newDir = path + "/" + folder
                removeFilesInCurrentFolder(newDir)
        print("deleting path " + path)
        os.rmdir(path)

removeFilesInCurrentFolder("D:/Downloads/test")