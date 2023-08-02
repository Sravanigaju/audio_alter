import os
from spleeter.separator import Separator

def vocal_isolation(input_file, output_dir):
    # Check if the output directory exists; if not, create it
    os.makedirs(output_dir, exist_ok=True)

    separator = Separator('spleeter:2stems')  # Load the 2stems (vocals and accompaniment) pre-trained model

    # Perform vocal isolation on the input audio file
    separator.separate_to_file(input_file, output_dir)

    print(f"Vocal isolation completed. Isolated tracks saved in {output_dir}.")

if __name__ == "__main__":
    input_file = r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't-Talk-Anymore.mp3"  # Replace with the path of your input file
    output_dir = r"C:\Users\Karthik Roy\audio_alter\audio_folder\We-Don't_vocaltest.mp3"  # Replace with the desired output directory path

    if os.path.getsize(input_file) > 50 * 1024 * 1024:
        raise ValueError("Input file size exceeds 50MB limit.")

    vocal_isolation(input_file, output_dir)
