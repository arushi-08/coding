class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # min path from top left to bottom right
        m = len(grid)
        n = len(grid[0])

        prev_n = [float('inf') for _ in range(n)]

        # base case:
        # if i==0, j==0, return grid[0][0]
        
        for i in range(m):
            curr = [float('inf') for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = grid[i][j]
                    continue
                
                elif j == 0:
                    curr[j] = prev_n[j] + grid[i][j]
                    continue
                elif i == 0:
                    curr[j] = curr[j-1] + grid[i][j]
                    continue

                curr[j] = min(prev_n[j], curr[j-1]) + grid[i][j]
            prev_n = curr
        
        print(curr)
        return curr[n-1]
