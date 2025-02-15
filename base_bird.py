

#tranform sound into mel spectogram, basic parameters for sound sampling and mfcc etc can be chosen ranomly and specified later 
#Create df with the and the spectorgram.
#question: should spectogram be stored in df or read from files?
#What the parameters should be?
#standardize spectograms
#padding at end of file.
#spectogram res?
def process_sound_file(file_path,label, segment_length):
    pass

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


