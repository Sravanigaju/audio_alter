import os
from pydub import AudioSegment
import pydub.effects as effects

def boost_bass(input_file, output_file, bass_boost_factor=10):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Calculate the cutoff frequency for the low pass filter
    sample_rate = audio.frame_rate
    bass_cutoff_frequency = 150  # Adjust this value to control the amount of bass boost

    # Apply the low pass filter to emphasize the lower frequencies (bass)
    boosted_audio = effects.low_pass_filter(audio, bass_cutoff_frequency)

    # Export the boosted audio to the output file with the appropriate format based on the file extension
    _, output_file_extension = os.path.splitext(output_file)
    output_file_extension = output_file_extension[1:].lower()  # Remove the dot and convert to lowercase

    supported_formats = ["mp3", "wav", "flac", "ogg"]

    if output_file_extension in supported_formats:
        boosted_audio.export(output_file, format=output_file_extension)
        print(f"Boosted audio saved as {output_file}")
    else:
        print(f"Unsupported output file format: {output_file_extension}")

if __name__ == "__main__":
    # Replace 'directory_name' with the actual directory where the input audio file is located.
    directory_name = 'audio_folder'

    # Replace 'input_song.mp3' with the actual name of your input audio file.
    input_filename = 'futuristic_beat.mp3'

    # Replace 'output_song_bass_boosted.mp3' with the desired output file name.
    output_filename = 'futuristic_beat_bass_boosted.flac'

    # Construct the full paths for input and output files using os.path.join
    input_file_path = os.path.join(os.curdir, directory_name, input_filename)
    output_file_path = os.path.join(os.curdir, directory_name, output_filename)

    boost_factor = 100  # You can adjust this value to control the amount of bass boost

    boost_bass(input_file_path, output_file_path, boost_factor)
