from tkinter import filedialog
import tkinter as tk

def GetFileFromUser():
    filepath = filedialog.askopenfilename()
    
def TkinterSetup():
    # Setup the Tkinter window
    root = tk.Tk()
    root.title("fGUIpg")
    root.minsize(450, 100)
    
    # Create a textbox to display the filepath
    filepath_entry = tk.Entry(root, width = 50)
    filepath_entry.pack(pady = 5)
    
    filepath_entry.insert(0, 'Select a file to continue')
    filepath_entry.config(state='disabled')
    
    # Create a button to trigger the file explorer prompt
    browse_button = tk.Button(root, text = "Browse", command = GetFileFromUser)
    browse_button.pack(padx = 180, pady = 10)
    
    root.mainloop()
    
def main():
    TkinterSetup()
    
if __name__ == "__main__":
    main()