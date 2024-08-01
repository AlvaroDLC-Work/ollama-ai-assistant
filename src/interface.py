import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from functions import *

eval_data = None
workfolder = None
search_value = None
file_path = None

def get_eval_data():
    global file_path
    global workfolder
    global eval_data
    
    file_path, workfolder, eval_data = open_file()
    
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, f"Eval Data: {file_path}\n{workfolder}\n{eval_data}\n ")
    
    return (file_path, workfolder, eval_data)

def get_process():
    # global file_path
    # global workfolder
    # global eval_data
    global search_value
    
    search_value = search_value.get()
    
    int_prompt, actual_responce, data_log_value = process_data(file_path, eval_data, workfolder,search_value)
    
    text_box.delete('1.0', tk.END)
    # text_box.insert(tk.END, f"Process: {file_path}\n{workfolder}\n{eval_data}\n{search_value} ")
    text_box.insert(tk.END, f"Process:\n | IntPrompt= {int_prompt} | \n | Responce= {actual_responce} | \n | Log={data_log_value}|\n ")

    
    # Call the imported function
    # messagebox.showinfo("Result", f"The result is: {result}")
    
    
def close_app():
    root.quit()

root = tk.Tk()
root.title("Personal Assistent")
root.geometry('850x500')

# Create a frame for the buttons and checkboxes
frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame,text="Termino de Busqueda")
label.grid(row=0, column=0, padx=5)

search_value = tk.Entry(frame,width=30 )
search_value.grid(row=0, column=1, padx=5)

# Open File button
open_button = tk.Button(frame, text="Open File", command=get_eval_data)
open_button.grid(row=1, column=0, padx=5)

# Process Data button
process_button = tk.Button(frame, text="Process Data", command=get_process)
process_button.grid(row=1, column=1, padx=5)

"""
# Clean Data button
clean_button = tk.Button(frame, text="Clean Data", command=clean_log_data)
clean_button.grid(row=0, column=2, padx=5)

# Copy Result button
copy_button = tk.Button(frame, text="Copy Result", command=copy_result)
copy_button.grid(row=0, column=3, padx=5)

# Close App button
close_button = tk.Button(frame, text="Close App", command=close_app)
close_button.grid(row=0, column=4, padx=5)



# Checkbuttons
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

check1 = tk.Checkbutton(frame, text="Uppercase", variable=var1)
check1.grid(row=1, column=0, pady=5)

check2 = tk.Checkbutton(frame, text="Lowercase", variable=var2)
check2.grid(row=1, column=1, pady=5)

check3 = tk.Checkbutton(frame, text="Title Case", variable=var3)
check3.grid(row=1, column=2, pady=5)
"""
# Text box to show result data
text_box = ScrolledText(root, wrap=tk.WORD, width=100, height=25)
text_box.pack(pady=10)

root.mainloop()

