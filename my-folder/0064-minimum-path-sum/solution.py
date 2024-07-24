class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        dp = [[0]*(col+1) for _ in range(row+1)]
        
        for i in range(row+1):
            dp[i][0] = float('inf')
        for i in range(col+1):
            dp[0][i] = float('inf')

        dp[1][1] = grid[0][0]

        for i in range(1, row+1):
            for j in range(1, col+1):
                if (i,j) != (1,1):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
                    # print(dp[i][j])
        # print(dp)
        return dp[row][col]
