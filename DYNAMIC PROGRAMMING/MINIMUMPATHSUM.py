# Recursion
def minPathSum(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0]) 
    return fun(grid, 0, 0, m, n)

def fun(grid, i, j, m, n):
    if i >= m or j >= n:
        return float('inf')
    
    if i == m - 1 and j == n - 1:
        return grid[i][j]
    
    right = fun(grid, i, j + 1, m, n)
    down = fun(grid, i + 1, j, m, n)

    return grid[i][j] + min(right, down)

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(grid))

# Memoization
def minPathSum(grid):
    if not grid:
        return 0
    
    dp = [[-1] * len(grid[0]) for _ in range(len(grid))] 
    m, n = len(grid), len(grid[0]) 
    return fun(grid, 0, 0, m, n, dp)

def fun(grid, i, j, m, n, dp):
    if i >= m or j >= n:
        return float('inf')
    if i == m - 1 and j == n - 1:
        return grid[i][j]
    
    if dp[i][j] != -1:
        return dp[i][j]

    right = fun(grid, i, j + 1, m, n, dp)
    down = fun(grid, i + 1, j, m, n, dp)

    dp[i][j] = grid[i][j] + min(right, down)
    return dp[i][j]

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(grid))

# Tabulation
def minPathSum(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:  # bottom-right corner
                dp[i][j] = grid[i][j]
            elif i == m - 1:  # last row, can only go right
                dp[i][j] = grid[i][j] + dp[i][j + 1]
            elif j == n - 1:  # last column, can only go down
                dp[i][j] = grid[i][j] + dp[i + 1][j]
            else:  
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
    
    return dp[0][0]

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(grid))
