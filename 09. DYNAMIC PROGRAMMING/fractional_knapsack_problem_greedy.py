def fractional_knapsack(items, capacity):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[2], reverse=True)
    total_value = 0
    knapsack = []

    for item in items:
        if capacity >= item[2]:  # If the whole item can fit
            knapsack.append((item[0], item[2]))
            total_value += item[1]
            capacity -= item[2]
        else:  # If only a fraction of the item can fit
            fraction = capacity / item[2]
            knapsack.append((item[0], fraction * item[2]))
            total_value += fraction * item[1]
            break  # Knapsack is full

    return total_value, knapsack

# Define items with their values and weights
items = [
    ("Stereo", 3000, 4),
    ("Laptop", 2000, 3),
    ("Guitar", 1500, 1),
    ("Necklace", 1000, 0.5)
]

# Define knapsack capacity
knapsack_capacity = 4

# Find the maximum value of goods and the items to steal
max_value, stolen_items = fractional_knapsack(items, knapsack_capacity)

# Display results
print("Maximum value of goods that can be stolen:", max_value)
print("Items stolen:")
for item in stolen_items:
    print("- {} (Weight: {:.2f} lbs)".format(item[0], item[1]))
