class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]
            nearest_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
            nearest_labels = [self.y_train[i] for i in nearest_indices]
            prediction = max(set(nearest_labels), key=nearest_labels.count)
            predictions.append(prediction)
        return predictions

    def _euclidean_distance(self, x1, x2):
        return sum((a - b) ** 2 for a, b in zip(x1, x2)) ** 0.5

# Example usage:
X_train = [[1, 2], [2, 3], [3, 4], [4, 5]]
y_train = [0, 0, 1, 1]

X_test = [[2, 2], [3, 3]]

knn = KNN(k=2)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

print("Predictions:", predictions)
