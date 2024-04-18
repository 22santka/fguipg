from tkinter import filedialog
import os
import ffmpy
from ffmpy import FFmpeg
import filefetch

def compressFile(input_file, output_file):
    # FFmpeg command for compression, then execute it
    ff = ffmpy.FFmpeg(inputs = {input_file: None}, outputs = {output_file: f"ffmpeg -i {input_file} -vcodec libx265 -crf 28 {output_file}"})
    
    ff.cmd
    ff.run()

def optimizeFile():
    if filefetch.filepath: 
        saveFileName = filedialog.asksaveasfilename(title="Save compressed file as", initialfile="compressed_video.mp4", defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        
        # Check if the user selected a save directory and file name, if so, make it. Else, give an error
        if saveFileName:
            outputFile = saveFileName
            compressFile(filefetch.filepath, outputFile)
            print("Video compression completed successfully!")
            print(outputFile)
        else:
            print("Please select a directory and provide a file name for saving the compressed video.")
    else:
        print("No video file selected.")

if __name__ == "__main__":
    optimizeFile()
