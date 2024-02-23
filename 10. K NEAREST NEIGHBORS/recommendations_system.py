from collections import defaultdict

# Movie preferences of users
users = {
    'Priyanka': {'Movie1', 'Movie2', 'Movie3', 'Movie4'},
    'Justin': {'Movie1', 'Movie2', 'Movie5', 'Movie6'},
    'JC': {'Movie2', 'Movie3', 'Movie4', 'Movie5'},
    'Joey': {'Movie1', 'Movie2', 'Movie6'},
    'Lance': {'Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'},
    'Chris': {'Movie3', 'Movie4', 'Movie5', 'Movie6'}
}

# Function to calculate similarity between users
def calculate_similarity(user1, user2):
    return len(user1.intersection(user2)) / len(user1.union(user2))

# Calculate similarity between Priyanka and other users
similarities = defaultdict(float)
for user, movies in users.items():
    if user != 'Priyanka':
        similarities[user] = calculate_similarity(users['Priyanka'], movies)

# Find top 5 most similar users to Priyanka
top_similar_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:5]

# Recommend movies liked by the most similar users to Priyanka
recommendations = set()
for user, _ in top_similar_users:
    recommendations.update(users[user])

print("Top 5 users most similar to Priyanka:", [user for user, _ in top_similar_users])
print("Movies recommended for Priyanka:", recommendations)
