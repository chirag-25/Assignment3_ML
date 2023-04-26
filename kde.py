import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs

# Generate some sample data
X, _ = make_blobs(n_samples=1000, centers=4, cluster_std=0.5, random_state=42)

# Estimate the bandwidth parameter using a KDE
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

# Fit the mean shift algorithm with the estimated bandwidth
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)

# Print the number of clusters and cluster centers
labels = ms.labels_
centers = ms.cluster_centers_
n_clusters = len(np.unique(labels))
print("Number of estimated clusters:", n_clusters)
print("Cluster centers:", centers)

# Plot the data points and cluster centers
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker='x', s=200, linewidths=3, color='r')
plt.show()
