import tkinter as tk
from pydub import AudioSegment
import os

# Constants
MAX_FILE_SIZE_MB = 50
FREQUENCY_BANDS = [60, 170, 310, 600, 1000, 3000, 6000, 12000, 14000, 16000]

# Function to apply the equalizer settings to the audio
def apply_equalizer(audio_file_path, gain_values):
    audio = AudioSegment.from_file(audio_file_path)
    for i, gain in enumerate(gain_values):
        band = FREQUENCY_BANDS[i]
        audio = audio.equalize(band, gain)
    return audio

# Function to update the equalizer settings and save the output
def update_equalizer():
    input_path = input_file_path.get()
    output_path = output_file_path.get()
    gain_values = [slider.get() for slider in gain_sliders]
    try:
        modified_audio = apply_equalizer(input_path, gain_values)
        modified_audio.export(output_path, format="mp3")
        status_label.config(text="Audio equalized and saved successfully.")
    except Exception as e:
        status_label.config(text="Error: " + str(e))

# Create the main application window
root = tk.Tk()
root.title("Audio Equalizer")

# Audio file path variables
input_file_path = tk.StringVar()
output_file_path = tk.StringVar()

# GUI elements
input_file_label = tk.Label(root, text=r"CC:\Users\Karthik Roy\audio_alter\audio_folder\futuristic_beat.mp3")
input_file_label.pack()

input_file_entry = tk.Entry(root, textvariable=input_file_path)
input_file_entry.pack()

output_file_label = tk.Label(root, text=r"C:\Users\Karthik Roy\audio_alter\audio_folder\futuristic_beat_equaloizer.mp3")
output_file_label.pack()

output_file_entry = tk.Entry(root, textvariable=output_file_path)
output_file_entry.pack()

gain_sliders = []
for i, band in enumerate(FREQUENCY_BANDS):
    slider_label = tk.Label(root, text=f"Band {i+1} - {band} Hz")
    slider_label.pack()
    slider = tk.Scale(root, from_=-10, to=10, orient=tk.HORIZONTAL, length=200, resolution=0.1)
    slider.pack()
    gain_sliders.append(slider)

apply_equalizer_btn = tk.Button(root, text="Apply Equalizer", command=update_equalizer)
apply_equalizer_btn.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Start the application
root.mainloop()