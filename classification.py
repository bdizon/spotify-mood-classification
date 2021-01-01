'''
Implement classification algorithms 
'''
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import svm

#svm helper functions

def svm(df):
    '''
    SVM
    Parameters: dataframe
    '''
    # print(type(df))
    df_feat = df[df.columns[0:7]]
    features = df_feat.to_numpy()
    # print(df)
    # print(features)
    target = df.mood.to_numpy()
    # print(target)

    # split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(features, target, train_size=0.8, random_state=0)

    # create SVM classifiers with different kernels and train models 
    linear = svm.SVC(kernel='linear', C=1, decision_function_shape='ovo').fit(X_train, y_train)
    rbf = svm.SVC(kernel='rbf', gamma=1, C=1, decision_function_shape='ovo').fit(X_train, y_train)
    poly = svm.SVC(kernel='poly', degree=3, C=1, decision_function_shape='ovo').fit(X_train, y_train)
    sig = svm.SVC(kernel='sigmoid', C=1, decision_function_shape='ovo').fit(X_train, y_train)

    # predict the classes for the test dataset
    linear_pred = linear.predict(X_test)
    poly_pred = poly.predict(X_test)
    rbf_pred = rbf.predict(X_test)
    sig_pred = sig.predict(X_test)

    # get accuracy for all kernels
    accuracy_lin = linear.score(X_test, y_test)
    accuracy_poly = poly.score(X_test, y_test)
    accuracy_rbf = rbf.score(X_test, y_test)
    accuracy_sig = sig.score(X_test, y_test)
    print("Accuracy Linear Kernel:", accuracy_lin)
    print("Accuracy Polynomial Kernel:", accuracy_poly)
    print("Accuracy Radial Basis Kernel:", accuracy_rbf)
    print("Accuracy Sigmoid Kernel:", accuracy_sig)
    return
    
def k_means():
    return

def decision_trees():
    return

def random_forest():
    return

def gradient_boosting():
    return

