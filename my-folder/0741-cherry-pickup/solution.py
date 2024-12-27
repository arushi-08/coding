class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        # assume 2 people are moving from 0,0 to m-1,n-1
        # both guys' steps
        n = len(grid)
        dp = [[[-float('inf')]*n for _ in range(n)] for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                for k in range(n-1,-1,-1):
                
                    l = max(0, min(i + j - k, n-1))
                    if i == n-1 and j == n-1 and k == n-1:
                        dp[i][j][k] = grid[i][j]
                        continue
                    if grid[i][j] == -1 or grid[k][l] == -1:
                        continue

                    cherries = 0
                    if i == k and j == l:
                        cherries += grid[i][j]
                    else:
                        cherries += grid[i][j] + grid[k][l]
                    
                    prev_cherries = -float('inf')
                    if i < n-1 and k < n-1:
                        prev_cherries = max(prev_cherries, dp[i+1][j][k+1])
                    if j < n-1 and l < n-1:
                        prev_cherries = max(prev_cherries, dp[i][j+1][k])
                    if j < n-1 and k < n-1:
                        prev_cherries = max(prev_cherries, dp[i][j+1][k+1])
                    if i < n-1 and l < n-1:
                        prev_cherries = max(prev_cherries, dp[i+1][j][k])

                    cherries += prev_cherries
                    if cherries != -float('inf'):
                        dp[i][j][k] = cherries

        if dp[0][0][0] == -float('inf'):
            return 0

        return dp[0][0][0]



    
