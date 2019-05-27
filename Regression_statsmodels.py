# %%
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
%matplotlib inline

# %%
dsPath = '/Users/housemex408/Google Drive/GWU/D.Eng/Praxis & Guidelines/Data Analysis/Datasets/D-Day Weather/'

# %%
weather = pd.read_csv(dsPath + 'Weather.csv', delimiter=',')

# %%
# X & Y are arrays of 1 element arrays
# https://stackoverflow.com/questions/18691084/what-does-1-mean-in-numpy-reshape
X = weather['MinTemp'].values.reshape(-1, 1)
y = weather['MaxTemp'].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# %%
# Does there appear to be a relationship?
# Do MinTemp & MaxTemp follow a normal distribution?
# https://seaborn.pydata.org/tutorial/distributions.html
sns.jointplot(x="MinTemp", y="MaxTemp", data=weather)

# %%
# Are there outliers?
plt.boxplot(X)
plt.title('MinTemp')
plt.show()

plt.boxplot(y)
plt.title('MaxTemp')
plt.show()

# %%
# Now lets train our model using Statsmodels
# http://www.statsmodels.org/dev/index.html
model = sm.OLS(y_train, X_train).fit()

# Add a constant term like so:
model = sm.OLS(y_train, sm.add_constant(X_train)).fit()
print(model.summary())
# %%
# Regression Plots:  https://www.statsmodels.org/dev/examples/notebooks/generated/regression_plots.html
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_regress_exog(model, "x1", fig=fig)
