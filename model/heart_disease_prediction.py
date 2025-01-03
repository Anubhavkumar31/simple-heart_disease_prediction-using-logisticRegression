# -*- coding: utf-8 -*-
"""Heart disease prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1txesDI-WpJHVNZpio6dWfoF4ZQTkN0lm

importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""data collection and processing"""

#loading the csv data to pandas dataframes
heart_data = pd.read_csv('/content/heart_disease_data.csv')

#print first 5 rows od dataset
heart_data.head()

#print 5 rows of dataset
heart_data.tail()

#number of rows and columns in dataset
heart_data.shape

#getting someinfo about the data
heart_data.info()

#checkinf for missing value
heart_data.isnull().sum()

#statistical measures about the data
heart_data.describe()

#checking the distribution of target value
heart_data['target'].value_counts()

"""1--->defective heart
0--->healthy heart

Splitting the features and target
"""

X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

print(X)

print(Y)

"""splitting the data into training and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2 )

print(X.shape, X_train.shape, X_test.shape)

"""model traning

LOGISTIC REGRESSION MODEL
"""

model = LogisticRegression()

#training the Logisticregression model with training data
model.fit(X_train, Y_train)

"""model evaluation accuracy score"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy o training data : ' , training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data : ' , test_data_accuracy)

"""building a predictive system"""

input_data = (40,0,1,130,204,0,0,172,0,1.4,5,0,2)

#change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for ony one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
  print('the person does not have a heart disease')
else:
  print('the person has heart disease')

