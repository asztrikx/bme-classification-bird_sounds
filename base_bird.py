

#tranform sound into mel spectogram, basic parameters for sound sampling and mfcc etc can be chosen ranomly and specified later 
#Create df with the and the spectorgram.
#question: should spectogram be stored in df or read from files?
#What the parameters should be?
#standardize spectograms
#padding at end of file.
#spectogram res?
'''
#Imports for process function
import os
import librosa
import librosa.display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
'''

'''
Create spectorgram dir for spectograms TODO discuss how to handle different runs
os.makedirs("spectrograms", exist_ok=True)'''

def process_sound_file(file_path, label, segment_length=3, sr=22050, n_mels=128, n_fft=2048, hop_length=512, save_dir="spectrograms"):

    y, sr = librosa.load(file_path, sr=sr)

    segment_samples = sr * segment_length
    num_segments = int(np.ceil(len(y) / segment_samples))

    spectrograms = []
    for i in range(num_segments):
        start = i * segment_samples
        end = start + segment_samples
        segment = y[start:end]

        #TODO how should padding work
        if len(segment) < segment_samples:
            segment = np.pad(segment, (0, segment_samples - len(segment)), mode='constant')

        mel_spec = librosa.feature.melspectrogram(y=segment, sr=sr, n_mels=n_mels, n_fft=n_fft, hop_length=hop_length)
        mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

        mel_spec_resized = cv2.resize(mel_spec_db, (128, 128))

        image_filename = f"{os.path.basename(file_path).replace('.ogg', '')}_seg{i}.png"
        image_path = os.path.join(save_dir, image_filename)
        plt.imsave(image_path, mel_spec_resized, cmap='inferno')

        spectrograms.append((image_path, label))

    return spectrograms

'''
#Example use of the process fv
data = []
file_path = "/content/XC163889.ogg"
label = "sparrow"
data.extend(process_sound_file(file_path, label))
df = pd.DataFrame(data, columns=["spectrogram_path", "label"])
'''


#iterate through train_meta_data and read the audiofiles with process_sound_file func.
#concetanate output dfs from process_sound_file into one df
#what is the longest sound file
#average length of sound files
def read_train_data(train_meta_df):
    pass

#Visualize spectogram with label showing which bird it belongs to
def vis_spectogram(spectogram, label):
    pass


#Be able to play the sound in notebook or other forms
def play_sound_file(file_path, label):
    pass


#TODO: dataloader, train-test-split, visualization


