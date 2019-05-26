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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Does there appear to be a relationship?
plt.scatter(X_train, y_train)
plt.title('MinTemp vs MaxTemp')  
plt.xlabel('MinTemp')  
plt.ylabel('MaxTemp')  
plt.show()
#%%
#Now lets train our model
regressor = LinearRegression()  
model = regressor.fit(X_train, y_train)
#%%
#Predict the response
y_pred = model.predict(X_test)

#%%
#Plot X and predicted Y line
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()
#%%
#Print out statistics
print('predicted response:', y_pred, sep='\n')
print('coefficient of determination:', metrics.r2_score(y_test, y_pred))
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


#%%
