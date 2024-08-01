from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import pyperclip
import os
import ollama
import datetime

"""
notas = '../data/notes.md'

with open (notas, 'r') as file:
content = file.read()
"""

def open_file():
  file_path = filedialog.askopenfilename()
  workfolder = os.path.dirname(file_path)
  if file_path:
    with open(file_path, 'r', encoding='utf-8') as file:
      eval_data = file.read()
  return (file_path, workfolder, eval_data)

def timestamp_format():
  timestamp_format = "%Y-%m-%d %H:%M:%S"
  timestamp = datetime.datetime.now().strftime(timestamp_format)
  return timestamp

def process_data(file_path, eval_data, workfolder,search_value):
  
  # Es la primera vez que lees esto En 10 palabras o menos. De las notas dime cual es: El plazo para la ejecución en numeral?
  
  # my_prompt = f' extrae todos los valores encerrados entre parentesis {content}'    
  int_prompt = f'Es la primera vez que lees esto {eval_data} (IP) Busca todo lo relacionado con {search_value}.\nDentro del siguiente texto: {eval_data}.(IP)'

  response = ollama.generate(model='qwen2:0.5b', prompt = int_prompt)
  
  actual_responce = response['response']
  
  data_log_value = data_log(file_path, workfolder, actual_responce, search_value)
  
  return (int_prompt, actual_responce, data_log_value)

def data_log(file_path, workfolder, actual_responce, search_value):
  timestamp = timestamp_format()
  # Combine the data with the timestamp
  data_log_value = f" \n {timestamp}\n P: Busca todo lo relacionado con: {search_value}.\n Dentro del siguiente arcvhivo: {file_path}\n R: {actual_responce}"
  
  with open(workfolder + "/log/Response_log.txt", "a", encoding="utf-8") as file:
      # Write the data to the file
      file.write(data_log_value + "\n")
  return data_log_value


def clean_log_data():
    # text_box.delete('1.0', tk.END)
    return

def copy_result():
    # content = text_box.get('1.0', tk.END)
    # pyperclip.copy(content)
    # messagebox.showinfo("Copy to Clipboard", "Result data copied to clipboard!")
    return

    # # Text box to show result data
    # text_box = ScrolledText(root, wrap=tk.WORD, width=60, height=20)
    # text_box.pack(pady=10)