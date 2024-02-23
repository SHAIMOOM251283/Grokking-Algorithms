def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1][2] > w:
                dp[i][w] = dp[i - 1][w]
            else:
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

def get_input():
    items = []
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        value = int(input("Enter item value: "))
        weight = int(input("Enter item weight: "))
        items.append((name, value, weight))
    return items

def main():
    print("Enter items for the knapsack:")
    items = get_input()
    capacity = int(input("Enter the knapsack capacity: "))
    max_value, selected_items = knapsack(items, capacity)

    print("\nMaximum value of items stolen:", max_value)
    print("Selected items:")
    for item in selected_items:
        print("- {} (${}, {} lbs)".format(item[0], item[1], item[2]))

if __name__ == "__main__":
    main()
