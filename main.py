'''
Visualize data set and compare classification algorithms using accuracy
'''
import pandas as pd
import numpy as np
import matplotlib as plt
from classification import *

# create dataframe
df_happy = pd.read_csv('data_files' + '\\' + 'happy_songs.csv')
df_sad = pd.read_csv('data_files' + '\\' + 'sad_songs.csv')
df_angry = pd.read_csv('data_files' + '\\' + 'angry_songs.csv')

# choose certain columns
df_happy1 = df_happy[df_happy.columns[2:20]].copy()
df_happy1.drop(["artist_uri","artist_name","genre","popularity","followers", 'key', 'liveness', 'time_signature'], axis=1, inplace=True)
print(df_happy1)
df_sad1 = df_sad[df_sad.columns[2:20]].copy()
df_sad1.drop(["artist_uri","artist_name","genre","popularity","followers", 'key', 'liveness', 'time_signature'], axis=1, inplace=True)
print(df_sad1)
df_angry1 = df_angry[df_angry.columns[2:20]].copy()
df_angry1.drop(["artist_uri","artist_name","genre","popularity","followers", 'key', 'liveness', 'time_signature'], axis=1, inplace=True)
print(df_angry1)

