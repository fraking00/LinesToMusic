import subprocess
from midi2audio import FluidSynth

def midi_to_wav(midi_file, soundfont_file, output_wav):
    try:
        fluidsynth_executable = "insert here fluidSynth.exe path"
        fs = FluidSynth(soundfont_file)

        # Construct the subprocess command
        command = [
            fluidsynth_executable, '-ni', fs.sound_font, midi_file, '-F', output_wav, '-r', str(fs.sample_rate)
        ]

        # Start the subprocess
        process = subprocess.Popen(command)
        process.communicate()

        # Check the return code
        if process.returncode == 0:
            print("Conversion from MIDI to WAV completed successfully.")
        else:
            print("Conversion from MIDI to WAV failed.")
    except Exception as e:
        print("An error occurred:", str(e))

