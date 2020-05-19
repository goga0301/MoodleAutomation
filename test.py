import os
from os import listdir

from os.path import isfile, join


def movefile():

    mypath = r"C:\Users\GOGA\Desktop\Java"
    onlydirs = [d for d in listdir(mypath) if os.path.isdir(join(mypath, d))]
    print(len(onlydirs))
    for d in onlydirs:
        if checkpptx(d) or d == "საკონტროლო 1" or d == "ჩატი (პირველი მცირე პროექტი)" or d == "შემაჯამებელი პროექტები":
            continue
        else:
            print(d)


def checkpptx(dir):
    path = f"C:/Users/GOGA/Desktop/Java/{dir}"
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(len(onlyfiles))
    for f in onlyfiles:
        if ".pptx" in f:
            bool = True
            return bool
        else:
            bool = False
    return bool


movefile()
