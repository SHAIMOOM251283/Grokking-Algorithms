import math

# User ratings for movie categories
priyanka_ratings = {'Comedy': 3, 'Action': 4, 'Drama': 4, 'Horror': 1, 'Romance': 4}
justin_ratings = {'Comedy': 4, 'Action': 3, 'Drama': 5, 'Horror': 1, 'Romance': 5}
morpheus_ratings = {'Comedy': 2, 'Action': 5, 'Drama': 1, 'Horror': 3, 'Romance': 1}
quentin_ratings = {'Comedy': 5, 'Action': 4, 'Drama': 5, 'Horror': 2, 'Romance': 3}
wes_ratings = {'Comedy': 4, 'Action': 3, 'Drama': 4, 'Horror': 1, 'Romance': 4}

# Define weights for influencers
quentin_weight = 2  # Quentin Tarantino's weight
wes_weight = 1.5    # Wes Anderson's weight

# Function to compute Euclidean distance between two vectors with weighted ratings
def euclidean_distance(vector1, vector2, weights):
    squared_difference = sum(((vector1.get(category, 0) - vector2.get(category, 0)) * weights.get(category, 1)) ** 2
                             for category in set(vector1) | set(vector2))
    return math.sqrt(squared_difference)

# Calculate Euclidean distance between Priyanka and other users with weighted ratings
distances = {
    'Justin': euclidean_distance(priyanka_ratings, justin_ratings, {}),
    'Morpheus': euclidean_distance(priyanka_ratings, morpheus_ratings, {}),
    'Quentin': euclidean_distance(priyanka_ratings, quentin_ratings, {'Comedy': quentin_weight, 'Action': quentin_weight, 'Drama': quentin_weight, 'Horror': quentin_weight, 'Romance': quentin_weight}),
    'Wes': euclidean_distance(priyanka_ratings, wes_ratings, {'Comedy': wes_weight, 'Action': wes_weight, 'Drama': wes_weight, 'Horror': wes_weight, 'Romance': wes_weight})
}

# Find the user with the smallest distance (most similar)
most_similar_user = min(distances, key=distances.get)

print("Most similar user to Priyanka based on Euclidean distance with weighted ratings:", most_similar_user)
