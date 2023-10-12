import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from grayscaleToMidi import grayscale_to_midi
from midiToWav import midi_to_wav
import os

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

        messagebox.showinfo("Conversion Complete", "Image to MIDI to WAV conversion completed successfully.")
    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("Image to MIDI Converter")

# Load the background image
background_image = Image.open("background_image.jpg")  # Replace with your image path
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas widget to display the background image
canvas = tk.Canvas(app, width=background_image.width, height=background_image.height)
canvas.pack()

# Display the background image on the Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

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
exit_button = tk.Button(app, text="Exit", command=app.quit)  # Add Exit button and define exit function


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
exit_button.pack()

app.mainloop()
