from pydub import AudioSegment
import soundfile as sf
import numpy as np
import os

def reduce_noise(input_file, output_file, noise_threshold=-35, chunk_size=5000):
    # Read the input audio file
    audio_format = input_file.split('.')[-1].lower()
    if audio_format in ('mp3', 'wav'):
        audio = AudioSegment.from_file(input_file, format=audio_format)
    elif audio_format in ('flac', 'ogg'):
        audio, sr = sf.read(input_file)
        audio = np.array(audio * 32767, dtype=np.int16)  # Convert to 16-bit PCM range
        audio = AudioSegment(audio.tobytes(), frame_rate=sr, sample_width=2, channels=1)
    else:
        raise ValueError("Unsupported file format. Supported formats: MP3, WAV, FLAC, OGG.")

    # Reduce noise using pydub's built-in noise reduction method
    audio = audio.reduce_noise(
        noise_threshold=noise_threshold,
        chunk_size=chunk_size,
        use_spectral_subtraction=True
    )

    # Save the processed audio to the output file
    output_format = output_file.split('.')[-1].lower()
    if output_format in ('mp3', 'wav'):
        audio.export(output_file, format=output_format)
    else:
        raise ValueError("Unsupported output file format. Supported formats: MP3, WAV.")

    print(f"Noise reduction completed. Output saved as {output_file}.")

if __name__ == "__main__":
    input_file = "input_file_path.mp3"  # Replace with the path of your input file
    output_file = "output_file_path.mp3"  # Replace with the desired output file path

    if os.path.getsize(input_file) > 50 * 1024 * 1024:
        raise ValueError("Input file size exceeds 50MB limit.")

    reduce_noise(input_file, output_file)
