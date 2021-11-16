import os
import shutil
import time

def removeFiles():
    path = "D:/Downloads/test"
    days = 0
    # seconds = time.time(days)
    seconds = time.time() - (days * 8640)

    if os.path.exists(path):
        for dir, folders, files in os.walk(path):
            if seconds >= ageOfFile(dir):
                removeFolder(dir)
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(dir, folder)
                    if seconds >= ageOfFile(folder_path):
                        removeFolder(folder_path)
                for file in files:
                    file_path = os.path.join(dir, file)
                    if seconds >= ageOfFile(file_path):
                        removeFile(file_path)


def ageOfFile(path):
    age = os.stat(path).st_ctime
    return age

def removeFolder(path):
    if not shutil.rmtree(path):
        print("{path} is removed successfully")
    else:
        print("Unable to delete the "+ path)

def removeFile(path):
    if not os.remove(path):
        print("{path} is removed successfully")
    else:
        print("Unable to delete the "+ path)