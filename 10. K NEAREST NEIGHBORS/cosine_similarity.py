import numpy as np

def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    similarity = dot_product / (norm_a * norm_b)
    return similarity

# Example vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Calculate cosine similarity
similarity = cosine_similarity(vector1, vector2)
print("Cosine Similarity:", similarity)
