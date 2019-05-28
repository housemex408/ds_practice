# %%
# https://www.slideshare.net/Simplilearn/machine-learning-with-python-machine-learning-algorithms-machine-learning-tutorial-simplilearn
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use("ggplot")

# %%
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

plt.scatter(x, y)
plt.show()

# %%
X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

# %%
colors = ["g.", "r."]

for i in range(len(X)):
    print("coordinate:", X[i], "label:",
          labels[i], "color:", colors[labels[i]])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

# : stands for beginning of first dimension, which is row
# [:, 0] means 1st row, 1st element
# [:, 1] means 1st row, 2nd element
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker="x", s=150, linewidths=5, zorder=10)

plt.show()


# %%
