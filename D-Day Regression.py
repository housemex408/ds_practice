#%%
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
%matplotlib inline

#%%
dsPath = '/Users/housemex408/Google Drive/GWU/D.Eng/Praxis & Guidelines/Data Analysis/Datasets/D-Day Weather/'

#%%
weather = pd.read_csv(dsPath + 'Weather.csv', delimiter = ',')

#%%
# X & Y are arrays of 1 element arrays
#https://stackoverflow.com/questions/18691084/what-does-1-mean-in-numpy-reshape
X = weather['MinTemp'].values.reshape(-1,1)
y = weather['MaxTemp'].values.reshape(-1,1)

# Does there appear to be a relationship?
plt.scatter(X, y)
plt.title('MinTemp vs MaxTemp')  
plt.xlabel('MinTemp')  
plt.ylabel('MaxTemp')  
plt.plot(X, y)
plt.show()
#%%
#Now lets train our model
regressor = LinearRegression()  
model = regressor.fit(X, y)

#%%
#To see what coefficients our regression model has chosen, execute the following script:
r_sq = model.score(X, y)

#%%
#Predict the response
y_pred = model.predict(X)

#%%
#Plot X and predicted Y line
plt.scatter(X, y)
plt.title('MinTemp vs MaxTemp')  
plt.xlabel('MinTemp')  
plt.ylabel('MaxTemp')  
plt.plot(X, y_pred, color='red')
plt.show()
#%%
#Print out statistics
print('predicted response:', y_pred, sep='\n')
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

#%%
