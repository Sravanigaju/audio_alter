from pysndfx import AudioEffectsChain
import librosa

# Function to apply reverb effect to an audio file
def apply_reverb(input_file, output_file):
    # Create an AudioEffectsChain with the reverb effect
    fx = AudioEffectsChain().reverb()

    # Load the audio file and the sample rate using librosa
    y, sr = librosa.load(input_file, sr=None)

    # Apply the reverb effect to the audio
    y_reverb = fx(y)

    # Save the processed audio to the output file
    librosa.output.write_wav(output_file, y_reverb, sr)

if __name__ == "__main__":
    # Replace these paths with the input and output file paths
    input_file_path = r'C:\Users\AICTE\OneDrive\Desktop\audio_alter\input\9.mp3'
    output_file_path = r'C:\Users\AICTE\OneDrive\Desktop\audio_alter\output\output_panned_audio1.mp3'

    # Apply the reverb effect to the audio file
    apply_reverb(input_file_path, output_file_path)