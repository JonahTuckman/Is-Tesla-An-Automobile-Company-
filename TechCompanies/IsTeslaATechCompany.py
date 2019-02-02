#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:16:20 2019

@author: JonahTuckman
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DataSet = pd.read_csv("FullDataSetTech.csv")
X = DataSet.iloc[:, 3:].values

Y = DataSet.iloc[:, 2].values
X_opt = X[:,[1,3,5,7,9]]

#from sklearn.model_selection import train_test_split
#X_train, X_test, Y_train, Y_test = train_test_split(X_opt, Y, test_size = 0.2, random_state = 0)



### Question:: have to do it this way because cannot be randomized?
## Must be in order because date is important
X_train = X_opt[:201]
X_test = X_opt[201:]
Y_train = Y[:201]
Y_test = Y[201:]


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

## Percentage is 66 Percent Accuracy

#Plot 


## Horrible graph because based on rise or fall, not trend
plt.plot(Y_train)
plt.plot(Y_test)
plt.plot(y_prediction)