import os
from pydub import AudioSegment

MAX_FILE_SIZE_MB = 50

def get_file_size_mb(file_path):
    return os.path.getsize(file_path) / (1024 * 1024)

def stereo_panner(input_file, output_file, pan):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Check if the audio file is stereo (2 channels)
    if audio.channels != 2:
        print("Error: Input file must be a stereo audio file (2 channels).")
        return

    # Ensure pan value is within the valid range (-1 to 1)
    pan = max(-1, min(1, pan))

    # Calculate the gain values for left and right channels
    left_gain = 1.0 - pan
    right_gain = 1.0 + pan

    # Apply panning to the audio
    audio = audio.split_to_mono()
    audio[0] = audio[0].apply_gain(left_gain)
    audio[1] = audio[1].apply_gain(right_gain)

    # Merge the left and right channels
    panned_audio = audio[0] + audio[1]

    # Export the panned audio to the output file
    output_format = output_file.split('.')[-1].lower()
    panned_audio.export(output_file, format=output_format)

if __name__ == "__main__":
    input_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't-Talk-Anymore.mp3"  # Change this to the path of your input audio file
    output_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\stereo_We-Don't-Talk-Anymore.mp3"  # Change this to the desired output file path
    pan = 1  # Pan value between -1 (left) and 1 (right)

    # Check if the file size is within the limit
    file_size_mb = get_file_size_mb(input_file)
    if file_size_mb > MAX_FILE_SIZE_MB:
        print(f"Error: File size exceeds the limit of {MAX_FILE_SIZE_MB}MB.")
    else:
        stereo_panner(input_file, output_file, pan)
