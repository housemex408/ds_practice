
#%%
from pandas import pandas as pd


#%%
dsPath = '/Users/housemex408/Google Drive/GWU/D.Eng/Praxis & Guidelines/Data Analysis/Datasets/California Civic/'

#%%
#Reading in data
props = pd.read_csv(dsPath + 'Committees.csv', delimiter = ',')


#%%
props.head()


#%%
props.info()


#%%
contribs = pd.read_csv(dsPath + 'Contributions.csv', delimiter = ',')


#%%
contribs.head()


#%%
contribs.info()


#%%
#Reading in columns
props.prop_name


#%%
props.prop_name.value_counts()


#%%
props.prop_name.value_counts().reset_index()


#%%
#Filtering
prop64 = props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

#%%
prop64.head()

#%%
prop64.info()

#%%
#Joining / Merging data
merged = pd.merge(prop64, contribs, on="calaccess_committee_id")


#%%
merged.head()

#%%
merged.info()

#%%
merged.amount

#%%
#Summing columns
merged.amount.sum()

#%%
merged.committee_position.value_counts()

#%%
support = merged[merged.committee_position == 'SUPPORT']
oppose = merged[merged.committee_position == 'OPPOSE']
#%%
oppose.amount.sum()
support.amount.sum()
support.amount.sum() / merged.amount.sum()

#%%
#Sorting
