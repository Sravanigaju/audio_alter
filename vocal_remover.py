from pydub import AudioSegment
import soundfile as sf
import numpy as np
import os

def vocal_cancellation(input_file, output_file):
    # Read the input audio file
    audio_format = input_file.split('.')[-1].lower()
    if audio_format in ('mp3', 'wav'):
        audio = AudioSegment.from_file(input_file, format=audio_format)
    elif audio_format in ('flac', 'ogg'):
        audio, sr = sf.read(input_file)
        audio = np.array(audio * 32767, dtype=np.int16)  # Convert to 16-bit PCM range
        audio = AudioSegment(audio.tobytes(), frame_rate=sr, sample_width=2, channels=2)
    else:
        raise ValueError("Unsupported file format. Supported formats: MP3, WAV, FLAC, OGG.")

    # Split the stereo audio into two separate mono channels
    left_channel, right_channel = audio.split_to_mono()

    # Invert the phase of one channel (to cancel out the center-panned vocals)
    instrumental = left_channel.overlay(right_channel.invert_phase())

    # Save the instrumental audio to the output file
    output_format = output_file.split('.')[-1].lower()
    if output_format in ('mp3', 'wav'):
        instrumental.export(output_file, format=output_format)
    else:
        raise ValueError("Unsupported output file format. Supported formats: MP3, WAV.")

    print(f"Vocal cancellation completed. Instrumental saved as {output_file}.")

if __name__ == "__main__":
    input_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't-Talk-Anymore.mp3"  # Replace with the path of your input file
    output_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't_vocalremover.mp3"  # Replace with the desired output file path

    if os.path.getsize(input_file) > 50 * 1024 * 1024:
        raise ValueError("Input file size exceeds 50MB limit.")

    vocal_cancellation(input_file, output_file)
