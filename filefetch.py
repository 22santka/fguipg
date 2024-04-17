from tkinter import filedialog
import os

class SelectFile:
    def __init__(self):
        pass
    isVideoFile = False
    
    def GetFileFromUser(self):
        filepath = filedialog.askopenfilename()
        
        if filepath:
            filename = os.path.basename(filepath)
            if filename.lower().endswith(".mp4"):
                # MainTkinterWindowSetup.filepath_label.config(text="Selected .mp4 file: " + filename)
                isVideoFile = True
                print(isVideoFile)
            else:
                # MainTkinterWindowSetup.filepath_label.config(text="ERROR: File does not have .mp4 extension type")
                isVideoFile = False
                print(isVideoFile)
                