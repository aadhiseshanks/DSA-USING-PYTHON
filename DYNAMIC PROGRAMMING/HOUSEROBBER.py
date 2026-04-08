# Recursion
def rob(nums, i):
    if i >= len(nums):
        return 0

    inc = nums[i] + rob(nums, i + 2)
    exc = rob(nums, i + 1)

    return max(inc, exc)

nums = [1, 10, 2, 4, 10, 5, 6, 1]
print(rob(nums, 0))

# Memoization
def rob(nums, dp, i):
    if i >= len(nums):
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    inc = nums[i] + rob(nums, dp, i + 2)
    exc = rob(nums, dp, i + 1)
    dp[i] = max(inc, exc)
    return dp[i]

nums = [1, 10, 2, 4, 10, 5, 6, 1]
dp = [-1] * len(nums)
print(rob(nums, dp, 0))

# Tabulation
def rob(nums, dp):
    for i in range(len(nums) - 1, -1, -1):
        inc = nums[i] + (dp[i + 2] if i + 2 < len(nums) else 0)
        exc = dp[i + 1] if i + 1 < len(nums) else 0
        dp[i] = max(inc, exc)
    return dp[0]

nums = [1, 10, 2, 4, 10, 5, 6, 1]
dp = [-1] * len(nums)
print(rob(nums, dp))
