import mido
from mido import MidiFile, MidiTrack, Message
import numpy as np

def grayscale_to_midi(image, output_file):
    with MidiFile() as midi_file:
        track = MidiTrack()
        midi_file.tracks.append(track)

        for row in image:
            for pixel_value in row:
                # Map pixel brightness to pitch
                pitch = int(np.interp(pixel_value, [0, 255], [40, 90]))

                # Map pixel brightness to note duration (arbitrary)
                duration = int(np.interp(pixel_value, [0, 255], [50, 200]))

                # Add a note message to the track
                track.append(Message('note_on', note=pitch, velocity=64, time=0))
                track.append(Message('note_off', note=pitch, velocity=64, time=duration))

        # Save the MIDI file
        midi_file.save(output_file)
