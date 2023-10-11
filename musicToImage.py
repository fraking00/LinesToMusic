import cv2
from grayscaleToMidi import grayscale_to_midi
from midiToWav import midi_to_wav
import os
from mido import MidiFile

# Ask the user for the path to the image they want to analyze
image_path = input("Enter the path to the image you want to analyze (e.g., 'input_image.jpg'): ")

# Load the user-specified image
image = cv2.imread(image_path)

# Ask the user for the desired size of the image
width = int(input("Enter the width of the image (e.g., 20): "))
height = int(input("Enter the height of the image (e.g., 30): "))

# Resize the image to the specified dimensions
resized_image = cv2.resize(image, (width, height))

# Convert the resized image to grayscale
grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Ask the user for the desired output MIDI file name
output_midi = input("Enter the name for the output MIDI file (e.g., 'output.mid'): ")

# Convert grayscale to MIDI with the custom MIDI file name
grayscale_to_midi(grayscale_image, output_midi)

# Ask the user for the desired output WAV file name
output_wav = input("Enter the name for the output WAV file (e.g., 'output.wav'): ")

# Convert the modified MIDI to WAV with the custom WAV file name
soundfont_file = 'D:/music_to_images/OPLLandOPLL2DrumFix2.sf2'
midi_to_wav(output_midi, soundfont_file, output_wav)
