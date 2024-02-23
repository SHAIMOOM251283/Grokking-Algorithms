import math

# User ratings for movie categories
priyanka_ratings = {'Comedy': 3, 'Action': 4, 'Drama': 4, 'Horror': 1, 'Romance': 4}
justin_ratings = {'Comedy': 4, 'Action': 3, 'Drama': 5, 'Horror': 1, 'Romance': 5}
morpheus_ratings = {'Comedy': 2, 'Action': 5, 'Drama': 1, 'Horror': 3, 'Romance': 1}

# Function to compute Euclidean distance between two vectors
def euclidean_distance(vector1, vector2):
    squared_difference = sum((vector1.get(category, 0) - vector2.get(category, 0)) ** 2
                             for category in set(vector1) | set(vector2))
    return math.sqrt(squared_difference)

# Calculate Euclidean distance between Priyanka and other users
distances = {
    'Justin': euclidean_distance(priyanka_ratings, justin_ratings),
    'Morpheus': euclidean_distance(priyanka_ratings, morpheus_ratings)
}

# Find the user with the smallest distance (most similar)
most_similar_user = min(distances, key=distances.get)

print("Most similar user to Priyanka based on Euclidean distance:", most_similar_user)
