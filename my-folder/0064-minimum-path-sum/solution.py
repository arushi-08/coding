class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # top left to bottom right
        # move down or right
        m = len(grid)
        n = len(grid[0])

        prev_n1 = [float('inf')] * n

        for i in range(m):
            prev_n2 = [float('inf')] * n
            for j in range(n):

                if i == 0 and j == 0:
                    prev_n2[j] = grid[i][j]
                
                else:
                    prev_n2[j] = min(prev_n1[j], prev_n2[j-1]) + grid[i][j]
            prev_n1 = prev_n2
        
        return prev_n1[n-1]

        # 1 3
