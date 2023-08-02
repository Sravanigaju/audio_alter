from pydub import AudioSegment
import os

def reverse_audio_file(input_file, output_file):
    # Check if the input file exists and has a supported extension
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    supported_formats = ['.mp3', '.wav', '.flac', '.ogg']
    file_extension = os.path.splitext(input_file)[1].lower()

    if file_extension not in supported_formats:
        print(f"Error: Unsupported file format '{file_extension}'.")
        return

    # Check the file size (Max 50MB)
    max_file_size = 50 * 1024 * 1024  # 50MB in bytes
    if os.path.getsize(input_file) > max_file_size:
        print("Error: File size exceeds the maximum limit of 50MB.")
        return

    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Reverse the audio
    reversed_audio = audio.reverse()

    # Export the reversed audio to the output file
    reversed_audio.export(output_file, format=file_extension[1:])
    print(f"Audio reversed and saved to '{output_file}'.")

if __name__ == "__main__":
    input_audio_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\futuristic_beat.mp3"  # Replace this with your input audio file
    output_audio_file = "output_audio_reverse.mp3"  # Replace this with the desired output filename

    reverse_audio_file(input_audio_file, output_audio_file)
