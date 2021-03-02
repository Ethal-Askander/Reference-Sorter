import tkinter as tk
from tkinter import filedialog, Text
import os
import re

def sort_references(references):
    '''
    @param references: a list of references
    
    @returns list of references in sorted alphabetical order

    Ignores all non-latin characters (sorts only bazed on a-z and A-Z)
    '''
    # Ignore all non-latin characters and sort
    references = sorted(references, key=lambda x: re.sub('[^A-Za-z]+', '', x).lower())
    
    # filter references
    filtered_references = ""
    for ref in references:
        # Check if empty string or just new line
        if (len(ref) == 0 or ref == "\n"):
            continue
        filtered_references += ref + ('\n\n' if ref != references[len(references) - 1] else '')
    return filtered_references

root = tk.Tk()
root.maxsize(700, 700)
root.minsize(700, 700)

# Defining GUI layout
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack(pady=10)

# Frame (inside) layout
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

text_box = tk.Text(canvas, height=40, fg="white", bg="#263D42")
text_box.pack()

def sort_clicked():
    '''
    Gets current text, sorts it and replaced the current text with the sorted text.
    '''
    # Get the references
    references = text_box.get("1.0", tk.END).split('\n')

    # Sort the references
    references = sort_references(references)

    text_box.replace("1.0", tk.END, references)

sort_button = tk.Button(root, text="Sort", padx=100, pady=5, fg="white", bg="black", command=sort_clicked)
sort_button.pack()

# Loop to run continously
root.mainloop()