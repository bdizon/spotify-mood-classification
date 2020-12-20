'''
Short code to combine .csv files containing song data and move all csv files to data_files folder
'''
import pandas as pd
import csv
import os
from os import listdir
import shutil
from pathlib import Path

def combine(csv_files, all_csv):
    '''
    Combines all the csv files into one csv file
    '''
    if len(all_csv) > 0:
        combined_csv = pd.concat([pd.read_csv(f,header=None) for f in csv_files])
        combined_csv.head()
        combined_csv.to_csv( "all_songs.csv", quotechar='"',
            quoting=csv.QUOTE_ALL, index=False, encoding='utf-8')
    return 

def find_all_csv():
    '''
    Find all csv files in current directory
    Return list of csv files
    '''
    # paths to current directory
    path_to_dir = os.getcwd()
    suffix = ".csv"
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith(suffix) ]

def move_files(csv_files):
    '''
    Move all csv files into data_files folder
    '''
    # paths to current directory and directory to data_files folder
    source_dir = os.getcwd()
    target_dir = source_dir + "\\" + "data_files"

    # convert path to right format
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)
    
    # move files to data_files
    for filename in csv_files:
        shutil.move(os.path.join(source_dir, filename), target_dir)
    return

csv_files = ['happy_songs.csv', 'sad_songs.csv','angry_songs.csv']
all_csv = find_all_csv()
combine(csv_files, all_csv)
all_csv = find_all_csv()
move_files(all_csv)