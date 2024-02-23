def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Iterate over each item (changing the order of rows won't affect the correctness)
    for i in range(1, n + 1):
        # Iterate over each possible weight capacity of the knapsack
        for w in range(1, capacity + 1):
            # Check if the weight of the current item exceeds the current capacity
            if items[i - 1][2] > w:
                # If so, the value of this cell remains the same as the value above it
                dp[i][w] = dp[i - 1][w]
            else:
                # Otherwise, choose the maximum value between including and excluding the current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][2]] + items[i - 1][1])

    # Backtrack to find the selected items
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][2]
        i -= 1

    return dp[n][capacity], selected_items


items = [
    ("Stereo", 3000, 4),
    ("Laptop", 2000, 3),
    ("Guitar", 1500, 1)
]

capacity = 4
max_value, selected_items = knapsack(items, capacity)

print("Maximum value of items stolen:", max_value)
print("Selected items:")
for item in selected_items:
    print("- {} (${}, {} lbs)".format(item[0], item[1], item[2]))
