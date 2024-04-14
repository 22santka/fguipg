import tkinter
import tkinter as tk   

class MainTkinterWindowSetup:   
    def __init__(self):
        pass     
    
    def changeValue(self):
        buttonClicked = False
        if buttonClicked:
            buttonClicked = False
        if not buttonClicked:
            buttonClicked = True
        
        
    def mainWindow(self):
        # Setup the Tkinter window
        app = tk.Tk()
        app.title("fGUIpg")
        app.minsize(500, 150)

        # Create a label to display the filepath
        filepath_label = tk.Label(app, text="Select a .mp4 file to continue")
        filepath_label.pack(pady=5)

        # Create a button to trigger the file explorer prompt
        browse_button = tk.Button(app, text = "Browse")
        browse_button.pack(padx = 180, pady = 10)

        # Create a button to optimize the video file
        compress_button = tk.Button(app, text = "Optimize")
        compress_button.pack(padx = 180, pady = 10)
        compress_button.config(state = "disabled")
 
        app.mainloop()