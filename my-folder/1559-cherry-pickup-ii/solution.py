class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        # again 2 robots - 4 indices
        m = len(grid)
        n = len(grid[0])
        dp = [[[-float('inf')]*n for _ in range(n)] for _ in range(m)]
        
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]

        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    cherries = 0
                    if j==k:
                        cherries += grid[i][j]
                    else:
                        cherries += grid[i][j] + grid[i][k]
                    # how many moves?
                    # i,j diagonal left, top, diagonal right, 
                    # 
                    prev_cherries = -float('inf')
                    if i > 0 and j > 0 and k > 0:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j-1][k-1]
                            )
                    if i > 0 and k > 0:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j][k-1]
                            )
                    if i > 0 and j < n-1 and k > 0:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j+1][k-1]
                            )
                    # 
                    if i > 0 and j > 0:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j-1][k]
                            )
                    if i > 0:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j][k]
                            )
                    if i > 0 and j < n-1:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j+1][k]
                            )
                    # 
                    if i > 0 and j > 0 and k < n-1:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j-1][k+1]
                            )
                    if i > 0 and k < n-1:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j][k+1]
                            )
                    if i > 0 and j < n-1 and k < n-1:
                        prev_cherries = max(
                            prev_cherries, dp[i-1][j+1][k+1]
                            )
                    
                    cherries += prev_cherries
                    dp[i][j][k] = cherries
        ans = 0
        for i in range(n):
            for j in range(n):
                ans = max(ans, dp[m-1][i][j])
        return ans
                    



