'''
Compare the classification algorithms
'''
import pandas as pd
import numpy as np
import matplotlib as plt
from classification import *

# create dataframe
df = pd.read_csv('data_files' + '\\' + 'all_songs.csv', encoding="utf-8", header=1) # get rid of first row
# choose specific audio feature columns
df = df[df.columns[7:20]].copy()
df.drop(['mode', 'instrumentalness','key', 'liveness', 'time_signature'], axis=1, inplace=True)

# check if mood column is free of errors
mood_dict = {}
for i in range(len(df.mood)):
    if df.mood[i] in mood_dict:
        mood_dict[df.mood[i]] += 1
    else:
        mood_dict[df.mood[i]] = 1
print(mood_dict)

# transform mood into integer classes
# 0 for angry, 1 for happy, 2 for sad
df.mood = pd.factorize(df.mood)[0]

# split dataset into features and targets
df_feat = df[df.columns[0:7]]
features = df_feat.to_numpy()
target = df.mood.to_numpy()

svm_acc = SVM(features, target)
# print(svm_acc)
