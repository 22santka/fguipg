# fGUIpg
fGUIpg is a program that adds a Tkinter based Python 3.0 GUI to the otherwise cmd line based FFmpeg. 
The purpose of this program is to add a quick, user friendly way to compress and lower the size of video files.

## Usage
> [!WARNING]
> On first startup, please launch the "requirementsdownload.py" file to download any of the nessecary packages required.

After the requirements have been downloaded, the program may be run directly from the "main.py" file.
There is no need to run the requirements check file a second time to use the program.

## Additional info
To update the version of FFmpeg that is used, download it from the source linked in the credits and replace the FFmpeg.exe file included in the program. <br />

# To-do list (As of 4/19/24):
Tier 1
- [x] Fix crashes for fresh installs
- [ ] Check and download program requirements automatically on startup
- [ ] Allow support for more video file types

Tier 2
- [ ] Compile program as an .exe file
- [ ] Compression options (User settings as top level element)
- [ ] Built in credits (As a top level element)

Tier 3
- [ ] Dark mode <br />

# Credits
- Tkinter, Guido van Rossum <guido@Python.org>, https://docs.python.org/3/library/tkinter.html
- FFmpeg, Fabrice Bellard; Bobby Bingham (libavfilter), & the FFmpeg team, https://ffmpeg.org/
- ffmpy, Copyright 2016, Andriy Yurchuk Revision 8a801925, https://ffmpy.readthedocs.io/en/latest/