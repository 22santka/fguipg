import tkinter
import tkinter as tk 
from filefetch import SelectFile # Imported class from another file

class MainTkinterWindowSetup:   
    def __init__(self):
        pass  
    applicationRunning = False
    browseButtonPressed = False
    compressButtonPressed = False
    
    def browseButton(self):       
        SelectFile.GetFileFromUser(SelectFile)

    def debugPrint():
        print("Browse button status:", MainTkinterWindowSetup.browseButtonPressed)
        print("Compress button status:", MainTkinterWindowSetup.compressButtonPressed)
            
    def mainWindow(self):
        # Setup the Tkinter window
        app = tk.Tk()
        app.title("fGUIpg")
        app.minsize(650, 300)
        MainTkinterWindowSetup.applicationRunning = True

        # Create a label to display the filepath
        filepath_label = tk.Label(app, text="Select a .mp4 file to continue")
        filepath_label.pack(pady=5)

        # Create a button to trigger the file explorer prompt
        browse_button = tk.Button(app, text = "Browse", command = lambda: MainTkinterWindowSetup.browseButton(self))
        browse_button.pack(padx = 180, pady = 10)

        # Create a button to optimize the video file
        compress_button = tk.Button(app, text = "Compress", command = lambda: MainTkinterWindowSetup.MainTkinterWindowSetup.buttonUpdate(MainTkinterWindowSetup.browseButtonPressed))
        compress_button.pack(padx = 180, pady = 10)
        compress_button.config(state = "disabled")
        
        # Create a debug button to print important info into the terminal
        compress_button = tk.Button(app, text = "debug print", command = lambda: MainTkinterWindowSetup.debugPrint())
        compress_button.pack(padx = 180, pady = 10)
            
        app.mainloop()     