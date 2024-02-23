def min_coins(amount, coins):
    num_coins = 0
    change = []

    # Sort coins in descending order
    coins.sort(reverse=True)

    for coin in coins:
        while amount >= coin:
            amount -= coin
            num_coins += 1
            change.append(coin)

    return num_coins, change

# Example: Making change for $1.27 using quarters, dimes, nickels, and pennies
amount = 127
coins = [25, 10, 5, 1]  # Quarter, dime, nickel, penny

min_num_coins, change = min_coins(amount, coins)
print("Minimum number of coins needed:", min_num_coins)
print("Change:", change)

# The greedy approach optimizes locally by selecting the largest possible coins at each step, 
# hoping to end up with the global optimum, which is the minimum number of coins needed to make the required change.
# The greedy algorithm for making change is easy to write and fast to run. 
# It doesn't require complex computations or extensive search, making it suitable for practical use. 
# However, it may not always produce the optimal solution, especially for certain coin systems where a non-greedy approach could yield a better result. 
# Nonetheless, for many scenarios, greedy algorithms serve as effective and efficient approximation algorithms.