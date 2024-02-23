def knapsack(items, capacity):
    n = len(items)
    # Scale the weights to integers
    scaled_items = [(name, value, int(weight * 10)) for name, value, weight in items]
    dp = [[0] * (capacity * 10 + 1) for _ in range(n + 1)]
    #dp = [[0.0] * (int(capacity * 10) + 1) for _ in range(n + 1)] ## Since you're converting weights to integers (int(weight * 10)) and the values are already accepted as floats, the floating-point initialization is not essential for functionality.

    for i in range(1, n + 1):
        for w in range(1, capacity * 10 + 1):
            if scaled_items[i - 1][2] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - scaled_items[i - 1][2]] + scaled_items[i - 1][1])

    # Backtrack to find the selected items
    selected_items = []
    i, w = n, capacity * 10
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= scaled_items[i - 1][2]
        i -= 1

    return dp[n][capacity * 10], selected_items

def get_input():
    items = []
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        value = float(input("Enter item value: "))
        weight = float(input("Enter item weight: "))  # Accept float input
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
        print("- {} (${}, {} lbs)".format(item[0], item[1], item[2] / 10))  # Scale weight back to original

if __name__ == "__main__":
    main()
