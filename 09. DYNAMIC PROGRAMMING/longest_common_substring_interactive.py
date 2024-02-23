def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a table to store lengths of longest common suffixes
    # Initialize a table to store lengths of longest common suffixes of substrings
    # where dp[i][j] stores the length of LCS of s1[0...i-1] and s2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # To store the length of the longest common substring
    max_length = 0
    
    # To store the ending index of the longest common substring
    end_index = 0
    
    # Fill dp table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0
                
    # Extract the longest common substring from s1
    longest_substring = s1[end_index - max_length: end_index]
    
    return longest_substring, max_length

def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")

    result, length = longest_common_substring(s1, s2)
    print("Longest common substring between '{}' and '{}' is '{}' with length {}.".format(s1, s2, result, length))

if __name__ == "__main__":
    main()
