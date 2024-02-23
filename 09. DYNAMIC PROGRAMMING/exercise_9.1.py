def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight, value = items[i - 1]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]
        i -= 1

    return dp[n][capacity], selected_items

items = [
    (3, 10),  # Water: 3 lb, 10 value
    (1, 3),   # Book: 1 lb, 3 value
    (2, 9),   # Food: 2 lb, 9 value
    (2, 5),   # Jacket: 2 lb, 5 value
    (1, 6)    # Camera: 1 lb, 6 value
]

capacity = 6
max_value, selected_items = knapsack(items, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
