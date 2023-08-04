from pydub import AudioSegment
import audioread
import os

def semitones_to_pitch_factor(semitones):
    return 2 ** (semitones / 12)

def change_pitch(input_file, output_file, semitones):
    # Load the audio file using pydub
    audio = AudioSegment.from_file(input_file)

    # Calculate the pitch factor from semitones
    pitch_factor = semitones_to_pitch_factor(semitones)

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
    input_file = input(r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't-Talk-Anymore.mp3")
    output_file = input(r"C:\Users\Karthik Roy\audio_alter\audio_folder\pitvh_We-Don't-Talk-Anymore.mp3")

    try:
        semitones = float(input("5"))
        if -20 <= semitones <= 20:
            validate_file_size(input_file, max_size_mb=50)
            change_pitch(input_file, output_file, semitones)
            print("Pitch change successful!")
        else:
            print("Invalid pitch change. Please enter a value between -20 and +20.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
