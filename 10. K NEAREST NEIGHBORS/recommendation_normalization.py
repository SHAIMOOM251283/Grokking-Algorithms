import math

# User ratings for movie categories
priyanka_ratings = {'Comedy': 3, 'Action': 4, 'Drama': 4, 'Horror': 1, 'Romance': 4}
justin_ratings = {'Comedy': 4, 'Action': 3, 'Drama': 5, 'Horror': 1, 'Romance': 5}
morpheus_ratings = {'Comedy': 2, 'Action': 5, 'Drama': 1, 'Horror': 3, 'Romance': 1}

# Function to normalize user ratings
def normalize_ratings(ratings):
    max_rating = max(ratings.values())
    min_rating = min(ratings.values())
    normalized_ratings = {}
    for category, rating in ratings.items():
        normalized_ratings[category] = (rating - min_rating) / (max_rating - min_rating)
    return normalized_ratings

# Function to compute Euclidean distance between two vectors with normalized ratings
def euclidean_distance(vector1, vector2):
    squared_difference = sum((vector1.get(category, 0) - vector2.get(category, 0)) ** 2
                             for category in set(vector1) | set(vector2))
    return math.sqrt(squared_difference)

# Normalize ratings for each user
priyanka_normalized = normalize_ratings(priyanka_ratings)
justin_normalized = normalize_ratings(justin_ratings)
morpheus_normalized = normalize_ratings(morpheus_ratings)

# Calculate Euclidean distance between Priyanka and other users with normalized ratings
distances = {
    'Justin': euclidean_distance(priyanka_normalized, justin_normalized),
    'Morpheus': euclidean_distance(priyanka_normalized, morpheus_normalized)
}

# Find the user with the smallest distance (most similar)
most_similar_user = min(distances, key=distances.get)

print("Most similar user to Priyanka based on Euclidean distance with normalized ratings:", most_similar_user)
