import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open (file_path,'r') as file:
            content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

app = tk.Tk()
app.title("File text reader")    

open_button = tk.Button(app,text="open file",command=open_file)
open_button.pack(pady=5)

text_area = tk.Text(app, wrap=tk.WORD)
text_area.pack(padx=5,pady=10,fill=tk.BOTH, expand=True)





            
