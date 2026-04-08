# Recursion
def climbstairs(n):
    if n == 0 or n == 1:
        return 1
    
    return climbstairs(n-1) + climbstairs(n-2)

n = int(input("Enter the number of stairs: "))
print(climbstairs(n))

# Memoization
def climbstairs(n, dp):
    if n == 0 or n == 1:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = climbstairs(n-1, dp) + climbstairs(n-2, dp)
    return dp[n]

n = int(input("Enter the number of stairs: "))
dp = [-1] * (n + 1)
print(climbstairs(n, dp))

# Tabulation
def climbstairs(n, dp):
    for i in range(0, n + 1):
        if i == 0 or i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input("Enter the number of stairs: "))
dp = [-1] * (n + 1)
print(climbstairs(n, dp)) 
