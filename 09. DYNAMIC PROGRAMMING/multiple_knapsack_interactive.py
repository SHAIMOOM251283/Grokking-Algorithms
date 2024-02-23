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
    print("Multiple Knapsack Problem Solver")

    num_items = int(input("Enter the number of items: "))
    items = []
    for i in range(num_items):
        value = int(input(f"Enter the value of item {i+1}: "))
        weight = int(input(f"Enter the weight of item {i+1}: "))
        items.append((value, weight))

    num_knapsacks = int(input("Enter the number of knapsacks: "))
    capacities = []
    for i in range(num_knapsacks):
        capacity = int(input(f"Enter the capacity of knapsack {i+1}: "))
        capacities.append(capacity)

    max_value, selected_items = multiple_knapsack(items, capacities)

    print("\nMaximum total value of items selected:", max_value)
    print("Items selected for each knapsack:")
    for i, knapsack_items in enumerate(selected_items):
        print(f"Knapsack {i + 1}:")
        for item in knapsack_items:
            print("- Value:", item[0], ", Weight:", item[1])

if __name__ == "__main__":
    main()
