import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

  
        sum_result = num1 + num2
        diff_result = num1 - num2
        average_result = (num1 + num2) / 2

        
        label_sum.config(text=f"Sum: {sum_result}")
        label_diff.config(text=f"Difference: {diff_result}")
        label_avg.config(text=f"Average: {average_result}")

    except ValueError:
       
        label_sum.config(text="Invalid Input")
        label_diff.config(text="Invalid Input")
        label_avg.config(text="Invalid Input")



app = tk.Tk()
app.title("Number Calculator")


entry_num1 = tk.Entry(app)
entry_num1.pack(pady=5)
entry_num2 = tk.Entry(app)
entry_num2.pack(pady=5)


calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.pack(pady=10)


label_sum = tk.Label(app, text="Sum:")
label_sum.pack()
label_diff = tk.Label(app, text="Difference:")
label_diff.pack()
label_avg = tk.Label(app, text="Average:")
label_avg.pack()

app.mainloop()
