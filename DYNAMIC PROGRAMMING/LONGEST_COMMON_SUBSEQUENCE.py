# Recursion
def lcs(str1, str2, i, j):
    if i >= len(str1) or j >= len(str2):
        return 0

    if str1[i] == str2[j]:
        return 1 + lcs(str1, str2, i + 1, j + 1)
    else:
        return max(lcs(str1, str2, i + 1, j), lcs(str1, str2, i, j + 1))
    
str1 = "abcde"
str2 = "ace"
print("Length of LCS is", lcs(str1, str2, 0, 0))

# Memoization
def lcs(str1, str2, i, j, dp):
    if i >= len(str1) or j >= len(str2):
        return 0
    
    if dp[i][j] != -1: return dp[i][j]

    if str1[i] == str2[j]:
        dp[i][j] = 1 + lcs(str1, str2, i + 1, j + 1, dp)
    else:
        dp[i][j] = max(lcs(str1, str2, i + 1, j, dp), lcs(str1, str2, i, j + 1, dp))
        
    return dp[i][j]
    
str1 = "abcde"
str2 = "ace"
dp = [[-1] * len(str2) for _ in range(len(str1))]
print("Length of LCS is", lcs(str1, str2, 0, 0, dp))

# Tabulation
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

str1 = "abcde"
str2 = "ace"
print("Length of LCS is", lcs(str1, str2))
