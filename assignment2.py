# -*- coding: utf-8 -*- changed file
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uLqr_xv_w9FyRqQyk7gDjuOH39EVvHXG
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

print('Booting into Machine Learning....')

data=pd.read_csv('/content/drive/MyDrive/hour.csv')

data.head(10)

print('Defining variables')
X = data['atemp']
y = data['registered']

plt.scatter(X,y, color='green')

print('Splitting the data into hour')
X_hour, X_test, y_hour, y_test = train_test_split(X,y,random_state=0)

plt.scatter(X_hour,y_hour, color='green')

plt.scatter(X_test,y_test, color='green')

print('Training the model using X_hour, y_hour')
lr = LinearRegression()

#print(X_hour)
#print(y_hour)
#print(X_hour.values.reshape(-1,1))
lr.fit(X_hour.values.reshape(-1,1),y_hour)

print('Predicting using the trained model - X_hour')
y_pred=lr.predict(X_test.values.reshape(-1,1))

print(y_test) #Test data - actual data
print(y_pred) #Model predicted dataset

plt.scatter(X_hour,y_hour,color='green')
plt.scatter(X_test,y_pred,color='red')

plt.xticks()
plt.yticks()
plt.show()

print('Finding intercept & coeff')
print('Intercept', lr.intercept_)
print('Coefficient', lr.coef_)
print(lr.coef_,'x +',lr.intercept_)
