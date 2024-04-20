# fGUIpg
fGUIpg is a program that adds a Tkinter based Python 3.0 GUI to the otherwise cmd line based FFmpeg. 

## Usage
> [!IMPORTANT]
> To use the program, please firstly download the required packages via the following command in your terminal:
```python
pip install -r requirements.txt
```
> This will download the package "ffmpy 0.3.2"

## Additional info
To update the version of FFmpeg that is used, download it from the source linked in the credits and replace the FFmpeg.exe file included in the program.
<br />

# To-do list (Last updated 4/19/24):
Tier 1
- [x] Fix crashes for fresh installs
- [ ] Support for more video file types, beyond just ".mp4"
- [ ] Allow support for more video file types

Tier 2
- [ ] Include requirements within the program, without the use of a terminal
- [ ] Compile program as an .exe file
- [ ] Compression options (User settings as top level element)
- [ ] Built in credits (As a top level element)

Tier 3
- [ ] Dark mode

<br />
# Credits
- Tkinter, Guido van Rossum <guido@Python.org>, https://docs.python.org/3/library/tkinter.html
- FFmpeg, Fabrice Bellard; Bobby Bingham (libavfilter), & the FFmpeg team, https://ffmpeg.org/
- ffmpy, Copyright 2016, Andriy Yurchuk Revision 8a801925, https://ffmpy.readthedocs.io/en/latest/