from tkinter import filedialog
import tkinter as tk   
import os

isVideoFile = False

def GetFileFromUser():
    filepath = filedialog.askopenfilename()
    if filepath:
        filename = os.path.basename(filepath)
        
        if filename.lower().endswith(".mp4"):
            filepath_label.config(text="Selected video file: " + filename)
            isVideoFile = True
            print(isVideoFile)
            
        else:
            filepath_label.config(text="ERROR: File does not have .mp4 extension type")
            isVideoFile = False
            print(isVideoFile)
    
def main():
    # Setup the Tkinter window
    root = tk.Tk()
    root.title("fGUIpg")
    root.minsize(500, 150)
    
    # Create a label to display the filepath
    global filepath_label
    filepath_label = tk.Label(root, text="Select a .mp4 file to continue")
    filepath_label.pack(pady=5)
    
    # Create a button to trigger the file explorer prompt
    browse_button = tk.Button(root, text = "Browse", command = GetFileFromUser)
    browse_button.pack(padx = 180, pady = 10)
    root.mainloop()
    
if __name__ == "__main__":
    main()