import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
from grayscaleToMidi import grayscale_to_midi
from midiToWav import midi_to_wav
import os
from music21 import stream  # Import the music21 library and stream object
from music21.note import Note

# Define a function to generate a simple polyphonic melody
def generate_polyphonic_melody(output_midi_filename):
    # Create a stream to hold the polyphonic composition
    composition = stream.Stream()

    # Create two simple melodies (voices)
    melody1 = stream.Part()
    melody2 = stream.Part()

    # Define the notes for each melody
    notes1 = ["C4", "E4", "G4", "A4", "C5"]
    notes2 = ["E3", "G3", "B3", "C4", "E4"]

    # Add notes to the first melody
    for note_name in notes1:
        note = Note(note_name)
        melody1.append(note)

    # Add notes to the second melody
    for note_name in notes2:
        note = Note(note_name)
        melody2.append(note)

    # Add the melodies to the composition
    composition.append(melody1)
    composition.append(melody2)

    # Save the composition to a MIDI file
    composition.write("midi", output_midi_filename)

# Update your convert_image function to include the polyphonic melody generation
def convert_image():
    image_path = entry_image_path.get()
    width = int(entry_width.get())
    height = int(entry_height.get())
    output_midi = entry_output_midi.get()
    output_wav = entry_output_wav.get()

    try:
        # Check if the image file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        # Load the user-specified image
        image = cv2.imread(image_path)

        # Resize the image to the specified dimensions
        resized_image = cv2.resize(image, (width, height))

        # Convert the resized image to grayscale
        grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Convert grayscale to MIDI
        grayscale_to_midi(grayscale_image, output_midi)

        # Convert MIDI to WAV
        soundfont_file = 'D:/music_to_images/OPLLandOPLL2DrumFix2.sf2'
        midi_to_wav(output_midi, soundfont_file, output_wav)

        # Generate a simple polyphonic melody
        generate_polyphonic_melody(output_midi)

        messagebox.showinfo("Conversion Complete", "Image to MIDI to WAV conversion completed successfully.")
    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("Image to MIDI Converter")

# Create and place labels, input fields, and buttons
label_image_path = tk.Label(app, text="Enter the path to the image you want to analyze (e.g., 'input_image.jpg'):")
entry_image_path = tk.Entry(app)
label_width = tk.Label(app, text="Enter the width of the image (e.g., 20):")
entry_width = tk.Entry(app)
label_height = tk.Label(app, text="Enter the height of the image (e.g., 30):")
entry_height = tk.Entry(app)
label_output_midi = tk.Label(app, text="Enter the name for the output MIDI file (e.g., 'output.mid'):")
entry_output_midi = tk.Entry(app)
label_output_wav = tk.Label(app, text="Enter the name for the output WAV file (e.g., 'output.wav'):")
entry_output_wav = tk.Entry(app)
convert_button = tk.Button(app, text="Convert", command=convert_image)

label_image_path.pack()
entry_image_path.pack()
label_width.pack()
entry_width.pack()
label_height.pack()
entry_height.pack()
label_output_midi.pack()
entry_output_midi.pack()
label_output_wav.pack()
entry_output_wav.pack()
convert_button.pack()

app.mainloop()
