import os
from pydub import AudioSegment
import pandas as pd
from tqdm import tqdm
import numpy as np

def aggregate_lengths(directory):
    # Define the directory path
    root_dir = directory
    # root_dir = '/home/dszarvas/projects/bme-classification-bird_sounds/data/train_audio'

    # Initialize an empty dictionary to store the results
    class_lengths = {}

    # Iterate through each class folder
    dir_list = os.listdir(root_dir)
    for i, class_name in enumerate(dir_list):
        print(f"Now processing class '{class_name}' ({i}/{len(dir_list)})")

        class_dir = os.path.join(root_dir, class_name)
        
        # Check if it's a directory
        if os.path.isdir(class_dir):
            total_length = 0
            
            # Iterate through each audio file in the class folder
            inner_pbar = tqdm(os.listdir(class_dir), desc=f'Processing {class_name}')
            for file_name in inner_pbar:
                if file_name.endswith('.ogg'):
                    file_path = os.path.join(class_dir, file_name)
                    audio = AudioSegment.from_ogg(file_path)
                    total_length += len(audio) / 1000  # Convert milliseconds to seconds
            
            # Store the total length for the class
            class_lengths[class_name] = total_length
        
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(list(class_lengths.items()), columns=['Class', 'Total Length (s)'])
    df.to_csv('class_lengths.csv', index=False)

    print(df)

def gather_length_and_size(directory, metadata_file='data/train_metadata.csv'):
    # Define the directory path
    root_dir = directory
    # root_dir = '/home/dszarvas/projects/bme-classification-bird_sounds/data/train_audio'

    # Load the existing metadata CSV
    metadata_csv = pd.read_csv(metadata_file)

    # Initialize empty lists to store the audio lengths and file sizes
    audio_lengths = []
    audio_file_sizes = []

    # Iterate through each row in the metadata CSV
    for index, row in tqdm(metadata_csv.iterrows(), total=len(metadata_csv)):
        # Get the filename from the row
        filename = row['filename']

        # Get the class name from the filename
        class_name = filename.split('/')[0]

        # Get the file path
        file_path = os.path.join(root_dir, filename)

        # Check if the file exists
        if os.path.exists(file_path):
            # Get the audio length
            audio = AudioSegment.from_ogg(file_path)
            audio_length = len(audio) / 1000  # Convert milliseconds to seconds

            # Get the file size
            file_size = os.path.getsize(file_path)

            # Append the audio length and file size to the lists
            audio_lengths.append(audio_length)
            audio_file_sizes.append(file_size)
        else:
            # If the file does not exist, append NaN values
            audio_lengths.append(np.nan)
            audio_file_sizes.append(np.nan)

    # Create new columns in the metadata CSV
    metadata_csv['audio_length'] = audio_lengths
    metadata_csv['file_size'] = audio_file_sizes

    # Save the updated metadata CSV
    metadata_csv.to_csv('train_metadata_updated.csv', index=False)

    print(metadata_csv.head()) 



if __name__ == "__main__":
    gather_length_and_size('/home/dszarvas/projects/bme-classification-bird_sounds/data/train_audio')