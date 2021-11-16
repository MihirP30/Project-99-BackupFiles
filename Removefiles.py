from genericpath import isfile
import os
import shutil
import time

def removeFilesInCurrentFolder(path):
    days = 30
    # seconds = time.time() - (days*60*60*24)
    seconds = time.time() - (1)

    if os.path.exists(path):
        age = fileAge(path)
        if age > seconds:
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

def fileAge(path):
    stats = os.stat(path)
    result = (time.time()-stats.st_mtime)
    return result

removeFilesInCurrentFolder("D:/Downloads/test")