import os
import soundfile as sf
import numpy as np
from scipy import signal

def add_reverb(input_file, output_file, room_size=0.5):
    # Load the audio file
    audio, sample_rate = sf.read(input_file)

    # Generate reverb impulse response
    reverb_length = int(sample_rate * room_size)
    reverb_ir = np.random.normal(0, 0.05, reverb_length)

    # Repeat the impulse response for each channel if audio is multi-channel
    if audio.ndim > 1:
        reverb_ir = np.tile(reverb_ir[:, np.newaxis], audio.shape[1])

    # Apply reverb effect using convolution
    audio_with_reverb = signal.convolve(audio, reverb_ir, mode='full')

    # Normalize the audio to avoid clipping
    max_amp = np.max(np.abs(audio_with_reverb))
    audio_with_reverb /= max_amp

    # Save the audio with reverb
    sf.write(output_file, audio_with_reverb, sample_rate)

if __name__ == "__main__":
    input_file_path = r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't-Talk-Anymore.mp3"  # Replace with the path to your input audio file
    output_file_path = r"C:\Users\Karthik Roy\audio_alter\audio_folder\reverb_We-Don't-Talk-Anymore.mp3" # Replace with the desired output path

    # Check the file size before processing
    if os.path.getsize(input_file_path) > 50 * 1024 * 1024:
        print("Error: File size exceeds 50MB.")
    else:
        room_size_factor = 10  # You can adjust the room size factor as needed
        add_reverb(input_file_path, output_file_path, room_size_factor)
        print("Reverb added and output file saved successfully.")
