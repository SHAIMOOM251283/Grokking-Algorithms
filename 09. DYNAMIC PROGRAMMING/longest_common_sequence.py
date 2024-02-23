def longest_common_subsequence(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Initialize a table to store lengths of LCS for all subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill up the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Length of LCS is the value in the bottom-right corner of the table
    lcs_length = dp[m][n]

    # Backtrack to construct the LCS itself
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the LCS since we're building it from the end
    lcs.reverse()

    return lcs_length, ''.join(lcs)

# Example usage:
seq1 = "ABCBDAB"
seq2 = "BDCAB"
length, lcs = longest_common_subsequence(seq1, seq2)
print("Length of LCS:", length)
print("Longest common subsequence:", lcs)
