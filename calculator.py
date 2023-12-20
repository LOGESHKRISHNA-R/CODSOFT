import tkinter as tk
from tkinter import messagebox
from tkinter import Label, Entry
from tkinter.font import Font
from easygui import *
from tkinter import *


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
        return

    operation = operation_var.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Division operation by zero is not allowed.")
            return
    else:
        messagebox.showerror("Error", "Invalid operation. Please choose +, -, *, or /.")
        return

    result_text.delete(1.0, tk.END)  
    result_text.insert(tk.END, f"{result}")

#main window
window = tk.Tk()
window.geometry("500x500") #size of the window by default
window.resizable(0,0)
window.title("Calculator")
operation_head= Label(window, text = 'Perform Calculations', font = 'Arial 12 bold').pack(pady=10)

#input widgets
entry_num1 = tk.Entry(window, width=10)
entry_num2 = tk.Entry(window, width=10)
operation_var = tk.StringVar()
operation_var.set('+')


#operation choices
operation_choices = ['+', '-', '*', '/']
operation_menu = tk.OptionMenu(window, operation_var, *operation_choices)


#result label
result_label = tk.Label(window, text="Result ",font='Arial 25 bold' )

#calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)

#Place widgets 
entry_num1 = Entry(window, textvariable = entry_num1,  width = 24, font='Arial 14 bold')
entry_num1.pack(pady=5)
operation_menu.pack(pady=5)
entry_num2 = Entry(window, textvariable = entry_num2,  width = 24, font='Arial 14 bold')
entry_num2.pack(pady=5)
calculate_button.pack(pady=10)
result_label.pack(pady=18)
result_text = Text(window, height=2, width=20, font='Arial 14 bold')
result_text.pack(pady=5)




window.mainloop()
