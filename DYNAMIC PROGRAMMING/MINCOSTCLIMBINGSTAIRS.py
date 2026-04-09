# Recursion
def fun(cost, i):
    if i >= len(cost):
        return 0
    
    step1 = cost[i] + fun(cost, i+1)
    step2 = cost[i] + fun(cost, i+2)

    return min(step1, step2)

cost = [10, 15, 20]
print(min(fun(cost, 0), fun(cost, 1)))

# Memoization
def fun(cost, dp, i):
    if i >= len(cost):
        return 0
    
    if dp[i] != -1: return dp[i]

    step1 = cost[i] + fun(cost, dp, i+1)
    step2 = cost[i] + fun(cost, dp, i+2)

    return min(step1, step2)

cost = [10, 15, 20]
dp = [-1] * len(cost)
print(min(fun(cost, dp, 0), fun(cost, dp, 1)))

# Tabulation
def fun(cost):
    n = len(cost)
    dp = [0] * (n + 2)
    
    for i in range(n - 1, -1, -1):
        if i >= len(cost): 
            dp[i] = 0
        else:
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

    return min(dp[0], dp[1])

cost = [10, 15, 20]
print(fun(cost))
