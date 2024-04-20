# fGUIpg
fGUIpg is a program that adds a Tkinter based Python 3.0 GUI to the otherwise cmd line based FFmpeg. 

## Usage
To use the program, please firstly download the required packages for the usage of the program via the following command in your terminal:

```python
pip install -r requirements.txt
```
> This will download the package "ffmpy 0.3.2", a requirement for the program to function.

## Additional info
To update the version of FFmpeg that is used, download it from the source linked in the credits and replace the FFmpeg.exe file included in the program.

# To-do list (Last updated 4/18/24):
Tier 3
- [ ] Fix crashes for fresh installs
- [ ] Include requirements within the program, without the use of a terminal
- [ ] FFmpeg compression options (User settings)
- [ ] Allow support for more video file types
- [ ] Credits top level button

Tier 2
- [ ] Settings top level button
- [ ] Compile as an .exe file

# Credits
- Tkinter, Guido van Rossum <guido@Python.org>, https://docs.python.org/3/library/tkinter.html
- FFmpeg, Fabrice Bellard; Bobby Bingham (libavfilter), & the FFmpeg team, https://ffmpeg.org/
- ffmpy, Copyright 2016, Andriy Yurchuk Revision 8a801925, https://ffmpy.readthedocs.io/en/latest/