import os
from pydub import AudioSegment
import pydub.effects as effects

# Explicitly specify the FFmpeg executable path
AudioSegment.ffmpeg = "path/to/ffmpeg"  # Replace "path/to/ffmpeg" with the actual path to ffmpeg executable

def boost_bass(input_file, output_file, bass_boost_factor=10):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Apply bass boost using pydub's bass_eq function
    boosted_audio = effects.bass_eq(audio, bass_boost_factor)

    # Export the boosted audio to the output file
    boosted_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    # Replace 'directory_name' with the actual directory where the input audio file is located.
    directory_name = 'audio_folder'

    # Replace 'input_song.mp3' with the actual name of your input audio file.
    input_filename = 'futuristic_beat.mp3'

    # Replace 'output_song_bass_boosted.mp3' with the desired output file name.
    output_filename = 'futuristic_beat_bass_boosted.mp3'

    # Construct the full paths for input and output files using os.path.join
    input_file_path = os.path.join(os.curdir, directory_name, input_filename)
    print(input_file_path)
    output_file_path = os.path.join(os.curdir, directory_name, output_filename)
    print(output_file_path)

    boost_factor = 10  # You can adjust this value to control the amount of bass boost

    boost_bass(input_file_path, output_file_path, boost_factor)
