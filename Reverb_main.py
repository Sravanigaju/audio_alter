import os
from pydub import AudioSegment
from pydub.generators import Reverb
from pydub.playback import play

def add_reverb(input_file, output_file, room_size_factor=2):
    # Maximum allowed file size in bytes (50MB)
    max_file_size_bytes = 50 * 1024 * 1024

    # Check if the input file size exceeds the limit
    if os.path.getsize(input_file) > max_file_size_bytes:
        print("File size exceeds the maximum limit of 50MB.")
        return

    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Calculate the reverb room size based on the room_size_factor
    room_size_ms = int(audio.duration_seconds * 1000 * room_size_factor)

    # Create a reverb effect with the calculated room size
    reverb = Reverb(room_size=room_size_ms)

    # Apply the reverb effect to the audio
    audio_with_reverb = audio.overlay(reverb)

    # Export the audio with reverb to the output file
    audio_with_reverb.export(output_file, format="mp3")

if __name__ == "__main__":
    # Replace 'directory_name' with the actual directory where the input audio file is located.
    directory_name = 'audio_folder'

    # Replace 'input_song.mp3' with the actual name of your input audio file.
    input_filename = 'input_audio.mp3'

    # Replace 'output_song_with_reverb.mp3' with the desired output file name.
    output_filename = 'output_audio_with_reverb.mp3'

    # Construct the full paths for input and output files using os.path.join
    input_file_path = os.path.join(os.curdir, directory_name, input_filename)
    output_file_path = os.path.join(os.curdir, directory_name, output_filename)

    # Adjust the room_size_factor as needed to control the reverb effect
    room_size_factor = 2

    add_reverb(input_file_path, output_file_path, room_size_factor)

    # Play the output audio with reverb
    play(AudioSegment.from_file(output_file_path))
