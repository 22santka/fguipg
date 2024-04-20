import tkinter
import tkinter as tk
import compression # Imported file
import filefetch # Imported file

class MainTkinterWindowSetup:   
    def __init__(self):
        pass
    
    def browseButton(self):  
        filefetch.doFileSelect()
        
        # Check to see if the selected file is valid, and update the GUI accordingly
        if filefetch.filename.lower().endswith(".mp4"): 
            compress_button.config(state = "normal")
            filename_label.config(text=filefetch.filename)
            filepath_label.config(text=filefetch.filepath)
        else:
            compress_button.config(state = "disabled")
            filepath_label.config(text="ERROR: Non mp4 file selected.")

    def debugPrint(self):
            print("DEBUG-INFO: filefetch.filename =", filefetch.filename)
            print("DEBUG-INFO: filefetch.filepath =", filefetch.filepath)
            
    def compressButton(self):
        compression.optimizeFile()
        
    def mainWindow(self):
        # Set button status to be global
        global title_label
        global filename_label
        global filepath_label
        global browse_button
        global compress_button
        global settings_button
        
        # Setup the Tkinter window
        app = tk.Tk()
        app.title("fGUIpg")
        app.minsize(650, 250)
        app.resizable(False, False)
        
        # Title lavel
        title_label = tk.Label(app, text = "fGUIpg")
        title_label.config(font=("TkDefaultFont", 30))
        title_label.place(anchor = "center", relx = 0.5, rely = 0.1)
        
        # Create a label to display the filename
        filename_label = tk.Label(app, text="Select an mp4 file to continue")
        filename_label.config(font=("TkDefaultFont", 10))
        filename_label.place(anchor = "center", relx = 0.5, rely = 0.25)
        
        # Create a label to display the filepath
        filepath_label = tk.Label(app, text="")
        filepath_label.config(font=("TkDefaultFont", 10))
        filepath_label.place(anchor = "center", relx = 0.5, rely = 0.35)

        # Create a button to trigger the file explorer prompt
        browse_button = tk.Button(app, text = "Browse", command = lambda: MainTkinterWindowSetup.browseButton(self))
        browse_button.place(anchor = "center", relx = 0.25, rely = 0.55, height = 50, width = 150)
        
        # Create a button to view credits
        settings_button = tk.Button(app, text = "Settings")
        settings_button.place(anchor = "center", relx = 0.5, rely = 0.55, height = 50, width = 150)
        
        # Create a button to change settings
        credits_button = tk.Button(app, text = "Credits")
        credits_button.place(anchor = "center", relx = 0.75, rely = 0.55, height = 50, width = 150)
        
        # Create a button to optimize the video file
        compress_button = tk.Button(app, text = "Compress", command = lambda: MainTkinterWindowSetup.compressButton(self))
        compress_button.place(anchor = "center", relx = 0.5, rely = 0.825, height = 50, width = 475)
        compress_button.config(state = "disabled")
            
        app.mainloop()     