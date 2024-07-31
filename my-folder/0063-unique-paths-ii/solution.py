class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[-1][-1]: return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * (cols+1) for _ in range(rows+1)]
        
        dp[rows-1][cols-1] = 1

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] += dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]
    
