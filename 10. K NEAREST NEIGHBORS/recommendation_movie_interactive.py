from math import sqrt

# Modified movie ratings by users
user_ratings = {
    'User1': {'Action': 4, 'Comedy': 5, 'Drama': 3, 'Horror': 2},
    'User2': {'Action': 3, 'Comedy': 4, 'Drama': 5, 'Horror': 1},
    'User3': {'Action': 5, 'Comedy': 2, 'Drama': 4, 'Horror': 3, 'Romance': 5}
}

# Function to compute Euclidean distance between two users
def euclidean_distance(user1, user2):
    common_movies = set(user1.keys()) & set(user2.keys())  # Get common movies between the two users
    if len(common_movies) == 0:
        return None  # No common movies to compare
    squared_diff = sum((user1[movie] - user2[movie]) ** 2 for movie in common_movies)
    distance = sqrt(squared_diff)
    return distance

# Function to get recommendations for a given user
def get_recommendations(user, user_ratings):
    distances = [(other_user, euclidean_distance(user_ratings[user], user_ratings[other_user]))
                 for other_user in user_ratings if other_user != user]
    distances.sort(key=lambda x: x[1])  # Sort users by distance
    recommendations = []
    for other_user, distance in distances:
        if distance is None:  # If no common movies, skip
            continue
        for movie in user_ratings[other_user]:
            if movie not in user_ratings[user]:  # Movie not already rated by the user
                recommendations.append((movie, user_ratings[other_user][movie]))
    return recommendations

# Function to display recommendations
def display_recommendations(recommendations):
    if recommendations:
        print("Recommendations:")
        for movie, rating in recommendations:
            print(f"{movie}: {rating}")
    else:
        print("No recommendations available.")

# Interactive command line interface
def main():
    print("Welcome to the Movie Recommendation System!")
    while True:
        target_user = input("Enter the username for which you want recommendations (or type 'exit' to quit): ")
        if target_user.lower() == 'exit':
            print("Exiting...")
            break
        if target_user not in user_ratings:
            print("User not found. Please enter a valid username.")
            continue
        recommendations = get_recommendations(target_user, user_ratings)
        display_recommendations(recommendations)

if __name__ == "__main__":
    main()
