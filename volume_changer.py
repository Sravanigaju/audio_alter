import os
from pydub import AudioSegment
from pydub.utils import mediainfo

def change_volume(input_path, output_path, db_change):
    # Check the file size
    file_size_mb = os.path.getsize(input_path) / (1024 * 1024)
    if file_size_mb > 50:
        raise Exception("File size exceeds 50MB limit.")

    # Load the audio file
    audio = AudioSegment.from_file(input_path)

    # Change the volume by the given db_change value
    audio = audio + db_change

    # Export the audio with the changed volume
    audio.export(output_path, format=mediainfo(input_path)['codec_name'])

if __name__ == "__main__":
    input_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\futuristic_beat.mp3"  # Replace with the path of your input audio file
    output_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\volume_changer_futuristic_.mp3"  # Replace with the desired output path
    db_change =   # Replace with the desired volume change value in dB

    try:
        change_volume(input_file, output_file, db_change)
        print("Volume change successful.")
    except Exception as e:
        print("Error:", str(e))
