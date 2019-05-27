
# %%
from pandas import pandas as pd
%matplotlib inline

# %%
dsPath = '/Users/housemex408/Google Drive/GWU/D.Eng/Praxis & Guidelines/Data Analysis/Datasets/California Civic/'

# %%
#Reading in data
props = pd.read_csv(dsPath + 'Committees.csv', delimiter=',')


# %%
props.head()


# %%
props.info()


# %%
contribs = pd.read_csv(dsPath + 'Contributions.csv', delimiter=',')


# %%
contribs.head()


# %%
contribs.info()


# %%
#Reading in columns
props.prop_name


# %%
props.prop_name.value_counts()


# %%
props.prop_name.value_counts().reset_index()


# %%
# Filtering
prop64 = props[props.prop_name ==
               'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

# %%
prop64.head()

# %%
prop64.info()

# %%
# Joining / Merging data
merged = pd.merge(prop64, contribs, on="calaccess_committee_id")


# %%
merged.head()

# %%
merged.info()

# %%
merged.amount

# %%
# Summing columns
merged.amount.sum()

# %%
merged.committee_position.value_counts()

# %%
support = merged[merged.committee_position == 'SUPPORT']
oppose = merged[merged.committee_position == 'OPPOSE']
# %%
oppose.amount.sum()
support.amount.sum()
support.amount.sum() / merged.amount.sum()

# %%
# Sorting
merged.sort_values("amount")

# %%
merged.sort_values("amount", ascending=False)

# %%
merged.sort_values("amount", ascending=False).head()

# %%
support.sort_values("amount", ascending=False).head()

# %%
oppose.sort_values("amount", ascending=False).head()

# %%
# Group By
merged.groupby("committee_name_x").amount.sum()

# %%
merged.groupby("committee_name_x").amount.sum().reset_index()

# %%
merged.groupby("committee_name_x").amount.sum(
).reset_index().sort_values("amount", ascending=False)

# %%
# Group By multiple fields
merged.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum(
).reset_index().sort_values("amount", ascending=False)

# %%
merged.groupby(["contributor_firstname", "contributor_lastname", "committee_position"]
               ).amount.sum().reset_index().sort_values("amount", ascending=False)

# %%
# Charts
top_supporters = support.groupby(
    ["contributor_firstname", "contributor_lastname"]
).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)

# %%
top_supporters.head(10)

# %%
top_supporters.amount.plot.bar()

# %%
chart = top_supporters.head(5).amount.plot.barh()
chart.set_yticklabels(top_supporters.contributor_lastname)

# %%
top_supporters['contributor_fullname'] = top_supporters.contributor_firstname + \
    " " + top_supporters.contributor_lastname
top_supporters.head()

# %%
chart = top_supporters.head(5).amount.plot.barh()
chart.set_yticklabels(top_supporters.contributor_fullname)

# %%


def combine_names(row):
    if row.contributor_fullname.startswith('SEAN PARKER'):
        return 'SEAN PARKER'
    return row.contributor_fullname


# %%
top_supporters['contributor_cleanname'] = top_supporters.apply(
    combine_names, axis=1)

# %%
top_supporters.groupby(
    "contributor_cleanname"
).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)

# %%
