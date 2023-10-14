@echo off

set "libraries=numpy music21 tk pydub pyaudio midi2audio opencv-python mido"

for %%i in (%libraries%) do (
    pip install %%i
)

echo Installation complete!
