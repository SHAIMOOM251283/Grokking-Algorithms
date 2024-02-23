def optimal_attractions(attractions, time_limit):
    n = len(attractions)
    # Initialize a table to store the maximum ratings
    dp = [[0] * (int(time_limit * 2) + 1) for _ in range(n + 1)]

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for t in range(1, int(time_limit * 2) + 1):
            # If the current attraction can fit into the time limit
            if attractions[i - 1]['Time'] <= t:
                # Choose the maximum between including the attraction and excluding it
                dp[i][t] = max(dp[i - 1][t], attractions[i - 1]['Rating'] + dp[i - 1][t - int(attractions[i - 1]['Time'])])
            else:
                # If the attraction cannot fit, exclude it
                dp[i][t] = dp[i - 1][t]

    # Trace back to find the attractions included in the itinerary
    selected_attractions = []
    i, t = n, int(time_limit * 2)
    while i > 0 and t > 0:
        # If the value at (i, t) is different from the value above it, it means the attraction was included
        if dp[i][t] != dp[i - 1][t]:
            selected_attractions.append(attractions[i - 1])
            t -= int(attractions[i - 1]['Time'])
        i -= 1

    return dp[n][int(time_limit * 2)], selected_attractions

def main():
    attractions = []
    num_attractions = int(input("Enter the number of attractions: "))
    for i in range(num_attractions):
        attraction = input("Enter the name of attraction {}: ".format(i + 1))
        time = float(input("Enter the time needed for attraction {} (half-days): ".format(i + 1)))
        rating = float(input("Enter the rating of attraction {} (out of 10): ".format(i + 1)))
        attractions.append({'Attraction': attraction, 'Time': time, 'Rating': rating})

    time_limit = float(input("Enter the time limit for the trip (days): "))

    max_rating, itinerary = optimal_attractions(attractions, time_limit)

    print("Maximum total rating of attractions in the itinerary:", max_rating)
    print("Itinerary:")
    for attraction in itinerary:
        print("- {} ({} half-days)".format(attraction['Attraction'], attraction['Time']))

if __name__ == "__main__":
    main()
