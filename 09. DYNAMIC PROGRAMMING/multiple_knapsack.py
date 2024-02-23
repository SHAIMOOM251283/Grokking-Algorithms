def multiple_knapsack(items, capacities):
    n = len(items)
    m = len(capacities)

    # Initialize a table to store the maximum values
    dp = [[[0] * (max(capacities) + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, max(capacities) + 1):
                if items[i - 1][1] <= k:
                    dp[j][i][k] = max(dp[j][i - 1][k], dp[j - 1][i - 1][k - items[i - 1][1]] + items[i - 1][0])
                else:
                    dp[j][i][k] = dp[j][i - 1][k]

    # Trace back to find the items included in the knapsacks
    selected_items = [[] for _ in range(m)]
    k = max(capacities)
    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            if dp[j][i][k] != dp[j][i - 1][k]:
                selected_items[j - 1].append(items[i - 1])
                k -= items[i - 1][1]

    return dp[m][n][max(capacities)], selected_items

def main():
    items = [
        (60, 10),  # (value, weight)
        (100, 20),
        (120, 30)
    ]
    capacities = [50, 60, 70]  # Capacities of the knapsacks

    max_value, selected_items = multiple_knapsack(items, capacities)

    print("Maximum total value of items selected:", max_value)
    print("Items selected for each knapsack:")
    for i, knapsack_items in enumerate(selected_items):
        print(f"Knapsack {i + 1}:")
        for item in knapsack_items:
            print("- Value:", item[0], ", Weight:", item[1])

if __name__ == "__main__":
    main()
