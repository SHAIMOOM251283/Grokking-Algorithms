import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity

# Example data
X_train = np.array([[1, 0, 1, 0],
                    [1, 1, 0, 1],
                    [0, 1, 0, 1],
                    [0, 0, 1, 1]])

X_test = np.array([[1, 1, 0, 0],
                   [0, 1, 1, 0]])

# Calculate cosine similarity between X_train and X_test
cosine_sim_matrix = cosine_similarity(X_train, X_test)

# Initialize KNN classifier using cosine similarity
K = 2  # Number of neighbors
knn = NearestNeighbors(n_neighbors=K, metric='cosine')
knn.fit(X_train)

# Find K nearest neighbors for each data point in X_test
distances, indices = knn.kneighbors(X_test)

# Print the results
for i in range(len(X_test)):
    print(f"Test instance {i+1}:")
    print(f"   Nearest neighbors indices: {indices[i]}")
    print(f"   Distances to nearest neighbors: {distances[i]}")
