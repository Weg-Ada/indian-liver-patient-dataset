# -*- coding: utf-8 -*-
"""ILPD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s6ib0wg5ei7lIDUoAoVusRImUZhKJX10
"""

# Commented out IPython magic to ensure Python compatibility.
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# % matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Importing libraries for building the neural network
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

from sklearn.utils import shuffle
from keras.optimizers import SGD
from sklearn.preprocessing import StandardScaler

from numpy import array
from numpy import argmax
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import confusion_matrix
from sklearn import svm

#excel_data = pd.read_excel('data/cleaned.xls', sheet_name = 'data')

from google.colab import files
uploaded = files.upload()

excel_data = pd.read_excel('cleaned.xls')
headers = excel_data.columns.values
excel_data.head()

excel_data.groupby('Diagnosis class').size()

diagnosis_classes = len(excel_data.groupby('Diagnosis class').size())
diagnosis_classes = [ str(x + 1) for x in range(diagnosis_classes)]
diagnosis_classes

excel_data = shuffle(excel_data)
# one hot encoding
for i in headers:
    le = LabelEncoder()
    le.fit(excel_data[str(i)])
    excel_data[str(i)] = le.transform(excel_data[str(i)])
    encoded = to_categorical(excel_data[str(i)])
    
    if len(encoded[0]) > 2 and i != 'Diagnosis class':
        insert_loc = np.where(headers==i)
        insert_loc = insert_loc[0][0]

        excel_data = excel_data.drop(columns = i)
        for label in range(len(encoded[0])):
            excel_data.insert(int(insert_loc), str(i) + "_" + str(label), encoded[:,label])

excel_data.head()

# sc = StandardScaler() 
# data = sc.fit_transform(excel_data)
# scaled_df = pd.DataFrame(excel_data, columns=headers)

# for i in headers:
#     excel_data[str(i)]= scaled_df[str(i)]
# data[' Age '], data['Alkphos'], data['sgpt'], data['sgot'],data['TP'],data['ALB'],data['TB'],data['DB'] = dt[' Age '], dt['Alkphos'], dt['sgpt'], dt['sgot'] ,dt['TP'],dt['ALB'],dt['TB'],dt['DB']
#data[' Age '] = dt[' Age ']

# X_data set with arguments
# Y_data set with diagnostick class

Y_data = excel_data['Diagnosis class']
X_data = excel_data.drop(columns = 'Diagnosis class')

X_data.head()

# ratio 1/2 to 1/2
X_train = X_data[:238]
Y_train = Y_data[:238]

X_test = X_data[238:]
Y_test = Y_data[238:]

kfold = [[X_train, Y_train, X_test, Y_test], [ X_test, Y_test, X_train, Y_train]]
cvscores = []

number_of_neurons = int(input("Enter the number of neurons: "))
momentum_value = float(input("Enter the momentum value: (0 means no moment, allowed floating point numbers) "))

model = Sequential()
model.add(Dense(units = 32,activation = 'relu',input_dim = 106)) # input layer
model.add(Dense(units = number_of_neurons, activation = 'relu')) # hidden layer
model.add(Dense(units = 8,kernel_initializer= 'normal', activation = 'softmax')) # output wyjściowa

for X_train, Y_train, X_test, Y_test in kfold:

    model.compile(optimizer= SGD(lr = 0.07, momentum=momentum_value),loss= 'sparse_categorical_crossentropy', metrics= ['accuracy'])
    model.fit(X_train, Y_train, epochs = 30,shuffle = True, verbose = 2, validation_data=(X_test, Y_test))
    scores = model.evaluate(X_test, Y_test, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))

model.summary()

# Run classifier, using a model that is too regularized to see
# the impact on the results
classifier = svm.SVC(kernel='linear', C=0.04)
y_pred = classifier.fit(X_train, Y_train).predict(X_test)
cnf_matrix = confusion_matrix(Y_test, y_pred)

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = np.round(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], 2)
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()


# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=diagnosis_classes,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=diagnosis_classes, normalize=True,
                      title='Normalized confusion matrix')

plt.show()