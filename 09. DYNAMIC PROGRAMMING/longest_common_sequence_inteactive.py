def longest_common_subsequence(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create a table to store lengths of LCS for all subproblems
    cell = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the LCS table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                cell[i][j] = cell[i - 1][j - 1] + 1
            else:
                cell[i][j] = max(cell[i - 1][j], cell[i][j - 1])

    # Read the LCS from the table
    lcs_length = cell[m][n]
    lcs = [""] * (lcs_length + 1)
    lcs[lcs_length] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs[lcs_length - 1] = seq1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif cell[i - 1][j] > cell[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

def main():
    seq1 = input("Enter the first sequence: ").upper()
    seq2 = input("Enter the second sequence: ").upper()

    lcs = longest_common_subsequence(seq1, seq2)
    length = len(lcs)

    print("Length of LCS:", length)
    print("Longest common subsequence:", lcs)

if __name__ == "__main__":
    main()
