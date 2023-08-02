from pydub import AudioSegment
import numpy as np
import os

from pydub.utils import mediainfo
def auto_panner(input_file, output_file, pan_amount=0.7):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Split the audio into left and right channels
    channels = audio.split_to_mono()
    left_channel = channels[0]
    right_channel = channels[1]

    # Calculate the pan amount for each channel
    pan_left = pan_amount  # Range from -1.0 (left) to 1.0 (right)
    pan_right = -pan_amount

    # Pan the audio channels
    left_channel = pan_audio_channel(left_channel, pan_left)
    right_channel = pan_audio_channel(right_channel, pan_right)

    # Merge the panned channels back into stereo
    panned_audio = left_channel.overlay(right_channel)

    # Export the panned audio to the output file
    panned_audio.export(output_file, format="mp3")  # You can also use "wav", "flac", or "ogg"

def pan_audio_channel(channel, pan_amount):
    # Convert the AudioSegment to numpy array
    samples = np.array(channel.get_array_of_samples())

    # Calculate the number of samples to shift based on pan_amount
    num_samples = len(samples)
    shift_amount = int(pan_amount * (num_samples / 2))

    # Apply the shift to the numpy array
    panned_samples = np.roll(samples, shift_amount)

    # Convert the numpy array back to AudioSegment
    panned_channel = AudioSegment(
        panned_samples.tobytes(),
        frame_rate=channel.frame_rate,
        sample_width=channel.sample_width,
        channels=1
    )
    return panned_channel
if __name__ == "__main__":
    # Replace 'input_audio.mp3' with the name of your input audio file.
    input_file_path = r'C:\Users\Karthik Roy\audio_alter\audio_folder\futuristic_beat.mp3'

    # Replace 'output_panned_audio.mp3' with the desired output file name.
    output_file_path = r'C:\Users\Karthik Roy\audio_alter\audio_folder\autopanner_futuristic_beat.mp3'

    # Adjust the pan_amount to control the intensity of the auto panner effect (0.0 to 1.0).
    pan_amount = 0.7

    # Check if input file exists, and create one if not found
    if not os.path.isfile(input_file_path):
        print(f"Input file '{input_file_path}' not found. Creating an empty audio file.")
        with open(input_file_path, 'wb') as f:
            f.write(b'')

    # Check if output file exists, and create one if not found
    if not os.path.isfile(output_file_path):
        print(f"Output file '{output_file_path}' not found. Creating an empty audio file.")
        with open(output_file_path, 'wb') as f:
            f.write(b'')
            
    # Apply the auto panner effect
    auto_panner(input_file_path, output_file_path, pan_amount)

    print("Auto Panner effect applied successfully.")
