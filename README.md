# fGUIpg
fGUIpg is a program that adds a Tkinter based Python 3.0 GUI to the otherwise cmd line based FFmpeg. 
The purpose of this program is to add a quick, user friendly way to compress and lower the size of video files.

## Usage
> [!WARNING]
> On first startup, please launch the `requirementsdownload.py` file to download any of the nessecary packages required. <br /> <br />
> The packages will be automatically downloaded to your DEFAULT python pip path. Please keep this in mind.

After the requirements have been downloaded, the program may be run directly from the "main.py" file.
There is no need to run the requirements check file a second time to use the program.

# To-do list (As of 4/20/24):
Tier 1
- [x] Fix crashes for fresh installs
- [ ] Improve the default compression done on video files
- [ ] Check and download program requirements automatically on startup
- [ ] Update GUI when a file is being compressed, to avoid confusion when things may freeze
- [ ] Allow support for more video file types
- [ ] Allow user to change the output file type

Tier 2
- [ ] Compile program as an .exe file
- [ ] Compression options (User settings as top level element)
- [ ] Built in credits (As a top level element)

Tier 3
- [ ] Organize files in the project, since the explorer is a bit cluttered currently 
- [ ] Dark mode <br />

# Credits
- Tkinter, Guido van Rossum <guido@Python.org>, https://docs.python.org/3/library/tkinter.html
- FFmpeg, Fabrice Bellard; Bobby Bingham (libavfilter), & the FFmpeg team, https://ffmpeg.org/
- ffmpy, Copyright 2016, Andriy Yurchuk Revision 8a801925, https://ffmpy.readthedocs.io/en/latest/ 