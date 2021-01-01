'''
Short code to combine .csv files containing song data and move all csv files to data_files folder
'''
import pandas as pd
import csv
import os
from os import listdir
import shutil
from pathlib import Path

def combine(all_csv, filename):
    '''
    Combines all the csv files into one csv file
    '''
    if len(all_csv) > 0:
        combined_csv = pd.concat([pd.read_csv(f,header=None) for f in all_csv])
        # combined_csv.head()
        combined_csv = combined_csv.drop_duplicates()
        combined_csv.to_csv( filename, quotechar='"', quoting=csv.QUOTE_ALL, index=False, encoding='utf-8')
        print("Combined all files")
    return 

def find_all_csv(path_to_dir):
    '''
    Find all csv files in current directory
    Return list of csv files
    '''
    # paths to current directory
    # path_to_dir = os.getcwd()
    suffix = ".csv"
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith(suffix) ]

def move_files(csv_files, source_dir, target_dir):
    '''
    Move all csv files into data_files folder
    '''
   
    # convert path to right format
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)

    # list of current csv files in the target folder
    current_files = find_all_csv(target_dir)
    
    # current_files = dict(current_files)
    files_to_add = []
    for i in range(len(current_files)):
        if (current_files[i] in csv_files):
            temp_target = str(target_dir)  + "\\" + str(current_files[i])
            new_target = Path(temp_target)
            print(new_target)
            shutil.os.remove(new_target) # delete file to update            
    # move files to data_files
    for filename in csv_files:
        shutil.move(os.path.join(source_dir, filename), target_dir)
    print("Moved all files to", str(target_dir))
    return

all_filename = "all_songs.csv"
# paths to current directory and directory to data_files folder
source_dir = os.getcwd()
target_dir = source_dir + "\\" + "data_files"

all_csv = find_all_csv(source_dir)
combine(all_csv, all_filename)
all_csv = find_all_csv(source_dir)
move_files(all_csv, source_dir, target_dir)