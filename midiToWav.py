import subprocess
from midi2audio import FluidSynth

def midi_to_wav(midi_file, soundfont_file, output_wav):
    fluidsynth_executable = "insert here the path to the .exe in this folder"
    fs = FluidSynth(soundfont_file)

    # Construct the subprocess command
    command = [
        fluidsynth_executable, '-ni', fs.sound_font, midi_file, '-F', output_wav, '-r', str(fs.sample_rate)
    ]

    # Start the subprocess
    process = subprocess.Popen(command)

    # Wait for the process to complete (block until it's done)
    process.communicate()

    # Check the return code (0 indicates success)
    if process.returncode == 0:
        print("Conversion from MIDI to WAV completed successfully.")
    else:
        print("Conversion from MIDI to WAV failed.")
