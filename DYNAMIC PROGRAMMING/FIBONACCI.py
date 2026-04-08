# Recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

n = int(input("Enter the value of n: "))
fib(n)

# Memoization
def fib(n, dp):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    if dp[n] != -1: # Check if the value is already computed
        return dp[n]
    
    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

n = 8
dp = [-1] * (n + 1)
fib(n, dp)

# Tabulation
def fib(n, dp):
    for i in range(0, n + 1):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = 8
dp = [-1] * (n + 1)
fib(n, dp)
