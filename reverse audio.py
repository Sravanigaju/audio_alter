from pydub import AudioSegment

def reverse_audio(input_path, output_path):
    # Load the audio file
    audio = AudioSegment.from_file(input_path)

    # Reverse the audio samples
    reversed_audio = audio.reverse()

    # Export the reversed audio to the output file
    reversed_audio.export(output_path, format="mp3")  # You can use "wav", "flac", "ogg", etc.

if __name__ == "__main__":
    input_audio_path =  r'C:\Users\AICTE\OneDrive\Desktop\audio_alter\input\9.mp3' # Replace with the path to your input audio file
    output_audio_path = r"C:\Users\AICTE\OneDrive\Desktop\audio_alter\output\revered_audio.mp3"  # Replace with the desired output path

    reverse_audio(input_audio_path, output_audio_path)
    print("Audio reversed and saved successfully.")
