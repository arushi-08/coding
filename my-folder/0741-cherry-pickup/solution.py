class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        # think of the 4d method
        # assume 2 people are moving from 0,0 to m-1,n-1

        # both guys' steps
        n = len(grid)
        dp = [[[-float('inf')]*n for _ in range(n)]for _ in range(n)]

        # row1, col1, row2, col2
        # 1,0 or 0,1
        
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
                    temp1, temp2 = 0,0
                    if i == k and j == l:
                        cherries += grid[i][j]
                        temp1 = grid[i][j]
                    else:
                        cherries += grid[i][j] + grid[k][l]
                        temp2 = grid[i][j] + grid[k][l]
                    
                    if i == n-1 or k == n-1:
                        f1 = -float('inf')
                    else:
                        f1 = dp[i+1][j][k+1]
                    if j == n-1 or l == n-1:
                        f2 = -float('inf')
                    else:
                        f2 = dp[i][j+1][k]
                    if j == n-1 or k == n-1:
                        f3 = -float('inf')
                    else:
                        f3 = dp[i][j+1][k+1]
                    if i == n-1 or l == n-1:
                        f4 = -float('inf')
                    else:
                        f4 = dp[i+1][j][k]
                    cherries += max(f1, f2, f3, f4)

                    if cherries != -float('inf'):
                        dp[i][j][k] = cherries

                    # print(dp[i][j][k], i, j, k, f1, f2, f3, f4, temp1, temp2)
        # print('dp', dp)
        if dp[0][0][0] == -float('inf'):
            return 0

        return dp[0][0][0]



    
