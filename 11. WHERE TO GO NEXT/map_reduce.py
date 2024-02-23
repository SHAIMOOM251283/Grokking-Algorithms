from collections import defaultdict
from multiprocessing import Pool

# Sample input data (list of sentences)
input_data = [
    "MapReduce is a programming model",
    "It is used for processing and generating large datasets",
    "MapReduce operates in parallel across distributed clusters"
]

def map_function(sentence):
    """Map function: splits each sentence into words and emits (word, 1) pairs"""
    word_count = defaultdict(int)
    words = sentence.split()
    for word in words:
        word_count[word] += 1
    return list(word_count.items())  # Convert dict_items to a list of tuples

def reduce_function(word_counts):
    """Reduce function: sums up the counts for each word"""
    word_count_total = defaultdict(int)
    for word, count in word_counts:
        word_count_total[word] += count
    return list(word_count_total.items())  # Convert dict_items to a list of tuples

def map_reduce(input_data):
    """MapReduce implementation"""
    # Map phase
    with Pool() as pool:
        mapped_data = pool.map(map_function, input_data)
    
    # Flatten the list of mapped data
    mapped_data_flat = [item for sublist in mapped_data for item in sublist]
    
    # Reduce phase
    word_count_total = reduce_function(mapped_data_flat)
    
    return word_count_total

if __name__ == "__main__":
    result = map_reduce(input_data)
    print("Word count result:")
    for word, count in result:
        print(f"{word}: {count}")
