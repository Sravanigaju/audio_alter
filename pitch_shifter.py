from pydub import AudioSegment
import audioread
import os

def change_pitch(input_file, output_file, pitch_factor):
    # Load the audio file using pydub
    audio = AudioSegment.from_file(input_file)

    # Change the pitch using the shift method in pydub
    pitched_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * pitch_factor)
    }).set_frame_rate(audio.frame_rate)

    # Export the pitched audio to the output file
    pitched_audio.export(output_file)

def validate_file_size(file_path, max_size_mb):
    # Check the size of the file in MB
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

    if file_size_mb > max_size_mb:
        raise ValueError(f"File size exceeds {max_size_mb}MB")

def main():
    input_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't-Talk-Anymore.mp3"  # Replace with the path to your input audio file
    output_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\pitch_We-Don't-Talk-Anymore.mp3"  # Replace with the desired output path
    pitch_factor = -1  # Adjust this to change the pitch (1.0 means no change)

    try:
        validate_file_size(input_file, max_size_mb=50)
        change_pitch(input_file, output_file, pitch_factor)
        print("Pitch change successful!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
