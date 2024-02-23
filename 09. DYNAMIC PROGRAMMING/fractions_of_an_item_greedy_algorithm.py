def thief(items, capacity):
    # Sort items by value per pound in descending order
    sorted_items = sorted(items, key=lambda x: x[1] / x[2], reverse=True)
    
    total_value = 0
    knapsack = []

    for item in sorted_items:
        if capacity >= item[2]:  # if the whole item fits
            knapsack.append((item[0], item[2]))
            total_value += item[1]
            capacity -= item[2]
        else:  # if only a fraction of the item fits
            fraction = capacity / item[2]
            knapsack.append((item[0], fraction * item[2]))
            total_value += fraction * item[1]
            capacity = 0
            break  # the knapsack is full
        
    return knapsack, total_value

# Test the function
items = [("Quinoa", 6, 2), ("Lentil", 3, 3), ("Rice", 2, 4)]
capacity = 5
knapsack, total_value = thief(items, capacity)
print("Items stolen:", knapsack)
print("Total value:", total_value)
