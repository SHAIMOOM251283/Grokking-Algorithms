def levenshtein_distance(s1, s2):
    # Create a matrix to store the distances
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],         # Deletion
                                   dp[i][j - 1],         # Insertion
                                   dp[i - 1][j - 1])    # Substitution

    # The bottom-right cell contains the Levenshtein distance
    return dp[m][n]

def main():
    print("Welcome to Levenshtein Distance Calculator!")
    while True:
        word1 = input("Enter the first word (or 'q' to quit): ").strip().lower()
        if word1 == 'q':
            print("Goodbye!")
            break
        word2 = input("Enter the second word: ").strip().lower()
        distance = levenshtein_distance(word1, word2)
        print(f"The Levenshtein distance between '{word1}' and '{word2}' is {distance}.")

if __name__ == "__main__":
    main()
