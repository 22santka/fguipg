from tkinter import filedialog
import os
import ffmpy
import filefetch

def compressFile(input_file, output_file):
    # Setup for the FFmpeg command variable
    output_path = os.path.abspath(output_file)
    input_path = os.path.abspath(input_file)
    
    # FFmpeg command for compression, then execute it. Potential update in the future for easy setting changes
    ffCmd = f'-y -i "{input_path}" -c:v libx265 -crf 28 -f mp4 "{output_path}"'
    ff = ffmpy.FFmpeg(inputs = {input_path: None}, outputs = {output_path: ffCmd})
    ff.run()

def optimizeFile():
    if filefetch.filepath: 
        saveFileName = filedialog.asksaveasfilename(title="Save compressed file as", initialfile="compressed_video.mp4", defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    
        if saveFileName:
            # Check if the user selected a save directory and file name, if so, make it. Else, give an error
            outputFile = saveFileName
            compressFile(filefetch.filepath, outputFile)
            print("Video compression completed successfully!")
        else:
            print("Please select a location and file name to save the compressed video.")

if __name__ == "__main__":
    optimizeFile()
