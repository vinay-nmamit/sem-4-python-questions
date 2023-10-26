#copy one file to another
import os
f1 = open("src.txt","r")
if os.path.exists("dst.txt"):
    print("file exists")
    f2 = open("dst.txt","w")
    for x in f1:
        f2.write(x)
else:
    print("file doesnot exists")
