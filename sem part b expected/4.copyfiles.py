#4.copy contents of one file to another
import os

f1 = open("src.txt","r")
if os.path.isfile("dst.txt"):
    print("File Exists")
else:
    f2 = open("dst.txt","a")
    for i in f1:
        f2.write(i)
    else:
        print("File Copied")
        f2.close()
f1.close()
