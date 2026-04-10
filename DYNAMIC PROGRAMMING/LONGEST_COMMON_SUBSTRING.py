# Recursion
def lcs(str1, str2, i, j, count):
    if i >= len(str1) or j >= len(str2):
        return count

    if str1[i] == str2[j]:
        count = lcs(str1, str2, i + 1, j + 1, count + 1)
    
    count = max(count, lcs(str1, str2, i + 1, j, 0))
    count = max(count, lcs(str1, str2, i, j + 1, 0))

    return count

str1 = "abcde"
str2 = "ace"
print("Length of LCS is", lcs(str1, str2, 0, 0, 0))

# Memoization
def lcs(str1, str2, i, j, count, dp):
    if i >= len(str1) or j >= len(str2):
        return count 

    if dp[i][j] != -1:
        return dp[i][j]

    temp = count
    if str1[i] == str2[j]:
        temp = lcs(str1, str2, i + 1, j + 1, count + 1, dp)
    
    temp = max(temp, lcs(str1, str2, i + 1, j, 0, dp))
    temp = max(temp, lcs(str1, str2, i, j + 1, 0, dp))

    dp[i][j] = temp
    return dp[i][j]


str1 = "abcde"
str2 = "abce"
dp = [[-1] * len(str2) for _ in range(len(str1))]

print("Length of LCS is", lcs(str1, str2, 0, 0, 0, dp))

# Tabulation
def lcs(str1, str2, i, j, count, dp):
    m, n = len(str1), len(str2)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


str1 = "abcde"
str2 = "abce"

# DP must be (m+1) x (n+1) to avoid index error
dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

print("Length of LCS is", lcs(str1, str2, 0, 0, 0, dp))
