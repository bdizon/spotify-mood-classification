'''
Implement classification algorithms 
'''
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix,  classification_report
from sklearn.model_selection import train_test_split
from sklearn import svm
import operator

#svm helper functions

def SVM(features, target):
    '''
    SVM
    Parameters: numpy array data features and targets
    Return: max accuracy 
    '''
    # split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(features, target, train_size=0.8, random_state=0)

    # create SVM classifiers with different kernels and train models 
    linear = svm.SVC(kernel='linear', C=1, decision_function_shape='ovo').fit(X_train, y_train)
    # linear = svm.SVC(kernel='linear').fit(X_train, y_train)
    rbf = svm.SVC(kernel='rbf', gamma=1, C=1, decision_function_shape='ovo').fit(X_train, y_train)
    poly = svm.SVC(kernel='poly', degree=3, C=1, decision_function_shape='ovo').fit(X_train, y_train)
    sig = svm.SVC(kernel='sigmoid', C=1, decision_function_shape='ovo').fit(X_train, y_train)

    # list of predicted values
    kernel_list = []
    # predict the classes for the test dataset
    linear_pred = linear.predict(X_test)
    kernel_list.append(linear_pred)
    poly_pred = poly.predict(X_test)
    kernel_list.append(poly_pred)
    rbf_pred = rbf.predict(X_test)
    kernel_list.append(rbf_pred)
    sig_pred = sig.predict(X_test)
    kernel_list.append(sig_pred)

    # get max from list of accuracies
    max_acc = []
    # get accuracy for all kernels
    accuracy_lin = linear.score(X_test, y_test)
    max_acc.append(accuracy_lin)
    accuracy_poly = poly.score(X_test, y_test)
    max_acc.append(accuracy_poly)
    accuracy_rbf = rbf.score(X_test, y_test)
    max_acc.append(accuracy_rbf)
    accuracy_sig = sig.score(X_test, y_test)
    max_acc.append(accuracy_sig)

    print("Accuracy Linear Kernel:", accuracy_lin)
    print("Accuracy Polynomial Kernel:", accuracy_poly)
    print("Accuracy Radial Basis Kernel:", accuracy_rbf)
    print("Accuracy Sigmoid Kernel:", accuracy_sig)

    index, value = max(enumerate(max_acc), key=operator.itemgetter(1))
    
    # create classification report for max accuracy
    print(classification_report(y_test,kernel_list[index]))
    return value
    
def k_means():
    return

def decision_trees():
    return

def random_forest():
    return

def gradient_boosting():
    return

