from tkinter import *
from tkinter import messagebox
import random 

global count
count = 0

root = Tk()
root.title("color changing button ")

colours = ["Blue","Red","Green","Yellow","Black","Purple","Pink","White","Brown","Orange"]

def colo():
    global count
    count += 1
    random.shuffle(colours)
    b.config(bg=str(colours[0]))
    if count % 5 == 0:
        messagebox.showinfo("5 clicks","5 clicks are done")
    
b = Button(root,text="Click me",command=colo,bg="pink")
b.grid(row=5,column=5)

root.mainloop()





    
