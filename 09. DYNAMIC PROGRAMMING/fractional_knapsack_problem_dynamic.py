def knapsack(items, capacity):
    n = len(items)
    # Initialize a table to store the maximum values
    dp = [[0] * (capacity * 10 + 1) for _ in range(n + 1)]

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for w in range(1, capacity * 10 + 1):
            # Convert the weight to an integer by multiplying by 10
            weight_int = int(items[i - 1][2] * 10)
            # If the current item can fit into the knapsack
            if weight_int <= w:
                # Choose the maximum between including the item and excluding the item
                dp[i][w] = max(dp[i - 1][w], items[i - 1][1] + dp[i - 1][w - weight_int])
            else:
                # If the item cannot fit, exclude it
                dp[i][w] = dp[i - 1][w]

    # Trace back to find the items included in the knapsack
    selected_items = []
    i, w = n, capacity * 10
    while i > 0 and w > 0:
        weight_int = int(items[i - 1][2] * 10)
        # If the value at (i, w) is different from the value above it, it means the item was included
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= weight_int
        i -= 1

    return dp[n][capacity * 10], selected_items

# Define items with their values and weights
items = [
    ("Stereo", 3000, 4),
    ("Laptop", 2000, 3),
    ("Guitar", 1500, 1),
    ("Necklace", 1000, 0.5)
]

# Define knapsack capacity
knapsack_capacity = 4

# Find the maximum value of goods that can be stolen and the items to steal
max_value, stolen_items = knapsack(items, knapsack_capacity)

# Display results
print("Maximum value of goods that can be stolen:", max_value)
print("Items stolen:")
for item in stolen_items:
    print("- {} (${}, {} lbs)".format(item[0], item[1], item[2]))

