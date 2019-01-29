#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:05:32 2019

@author: JonahTuckman
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Tesla = pd.read_csv("TSLA.csv")
#XTes = Tesla.iloc[:, 1:7]

#GeneralMotors = pd.read_csv("GM.csv")
#Honda = pd.read_csv("HMC.csv")
#Toyota = pd.read_csv("TM.csv")
#FiatChrys = pd.read_csv("FCAU.csv")

DataSet = pd.read_csv("FullDataSet.csv")
X = DataSet.iloc[:, 3:].values

Y = DataSet.iloc[:, 2].values
X_opt = X[:,[1,3,5,7,9]]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_opt, Y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

y_prediction = regressor.predict(X_test)
output= []
for i in y_prediction:
    output.append(np.sign(i))

# accuracy
count = 0
for i in range(50):
    if Y_test[i] == output[i]:
        count += 1
percent = (count / 50) * 100
print('%d Percent Accuracy' % percent)

## Prediction Results in 54% Accuracy