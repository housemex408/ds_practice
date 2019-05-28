# %%
# https://www.datascience.com/blog/k-means-clustering
# based on the result, we can infer that Group A is urban drivers and Group B is rural drivers
from sklearn.cluster import KMeans
from pandas import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use("ggplot")

# %%
dsPath = '/Users/housemex408/Google Drive/GWU/D.Eng/Praxis & Guidelines/Data Analysis/Datasets/Delivery Fleet/'

# %%
#Reading in data
df = pd.read_csv(dsPath + 'delivery_fleet.txt', delimiter='\t')
df.head(5)

f1 = df['Distance_Feature'].values
f2 = df['Speeding_Feature'].values
# %%
# populate into list and plot:  https://www.w3schools.com/python/python_lists.asp
length = len(f1)
dataList = []
for i in range(length):
    dataList.append([f1[i], f2[i]])
    plt.scatter(f1[i], f2[i])
plt.xlabel('distance')
plt.ylabel('speeding')
plt.title('Distance ~ Speeding')
plt.show()

#print("datalist:", dataList)

# %%
X = np.array(dataList)
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

# %%
colors = ["g.", "y."]

for i in range(len(X)):
    print("coordinate:", X[i], "label:",
          labels[i], "color:", colors[labels[i]])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

# : stands for beginning of first dimension, which is row
# [:, 0] means 1st row, 1st element
# [:, 1] means 1st row, 2nd element
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker="x", s=150, linewidths=5, zorder=10)

plt.xlabel('distance')
plt.ylabel('speeding')
plt.title('Distance ~ Speeding')
plt.show()


# %%
