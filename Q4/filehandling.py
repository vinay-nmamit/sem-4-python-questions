#to search .py files
import os

for i in os.listdir():
    if i.endswith('.py'):
        print(i)

#to count no of lines in a file
filename = input("enter name: ")
f = open(filename, "r")
i = 0
line = f.readline()

while line:
    i += 1
    line = f.readline()

print("Number of lines in the file:", i)
f.close()

