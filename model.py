# -*- coding: utf-8 -*-
"""UAS BIML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bet-8mX_PcOzT-EGH5SVbFp6AJeBLl77
"""

# Import libraries
## Basic libs
import pandas as pd
import numpy as np
#library
import joblib
from sklearn.linear_model import LinearRegression
# Load dataset
data = pd.read_excel('data.hotel.xlsx')

X = np.array(data.iloc[:, 1]).reshape((-1, 1))
y = np.array(data.iloc[:, 2])

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Import library pandas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

#Fitting model with trainig data
regressor.fit(X.values, y)

import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[99, 82]]))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[99, 82]]))