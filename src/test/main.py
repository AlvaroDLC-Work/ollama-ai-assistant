import tkinter as tk
from tkinter import messagebox
from process import process_data  # Import the process_data function

# Function to get input values and call process_data
def handle_process_data():
    value1 = entry1.get()
    value2 = entry2.get()
    content = (value1, value2)  # Package the values as a tuple or any other structure
    result = process_data(content)  # Call the imported function
    messagebox.showinfo("Result", f"The result is: {result}")

# Create the main window
root = tk.Tk()
root.title("Data Processing")

# Create a frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Add input fields
tk.Label(frame, text="Value 1:").grid(row=0, column=0, padx=5)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Value 2:").grid(row=1, column=0, padx=5)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=5)

# Add the process button
process_button = tk.Button(frame, text="Process Data", command=handle_process_data)
process_button.grid(row=2, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
