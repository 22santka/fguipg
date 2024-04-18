from tkinter import filedialog
import os

def doFileSelect():    
    global filepath
    filepath = filedialog.askopenfilename()

    if filepath:
        global filename
        filename = os.path.basename(filepath)