
from pydub import AudioSegment
from pydub.utils import make_chunks
import os

def add_reverb(input_file, output_file, room_size=1.0):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Apply reverb
    audio_with_reverb = audio.overlay(audio, position=0, gain_during_overlay=room_size)

    # Export the audio with reverb
    audio_with_reverb.export(output_file, format="mp3")  # You can change the format if needed

if __name__ == "__main__":
    input_file_path = r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't-Talk-Anymore.mp3"  # Replace with the path to your input audio file
    output_file_path = r"C:\Users\Karthik Roy\audio_alter\audio_folder\reverb_We-Don't-Talk-Anymore.mp3"

    # Check the file size before processing
    if os.path.getsize(input_file_path) > 50 * 1024 * 1024:
        print("Error: File size exceeds 50MB.")
    else:
        room_size_factor =   # You can adjust the room size factor as needed
        add_reverb(input_file_path, output_file_path, room_size_factor)
        print("Reverb added and output file saved successfully.")
