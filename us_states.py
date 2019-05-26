
#%%
import numpy as np
import pandas as pd
#%%
df = pd.read_csv('../Datasets/us-education-datasets-unification-project/states_all.csv', delimiter = ',')
#%%
df.head(10)
#%%
##df.describe()


#%%
df['FEDERAL_REVENUE'].hist(bins=50)

#%%
df['FEDERAL_REVENUE'].value_counts()

#%%
df.boxplot(column='FEDERAL_REVENUE')

#%%
df.boxplot(column='FEDERAL_REVENUE', by = 'STATE')

#%%


#%%
