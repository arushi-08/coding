from collections import deque
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        rows = [1, 0, -1, 0]
        cols = [0, -1, 0, 1]

        def dfs(grid, i, j, visited):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
                return 0
            
            maxgold = 0 
            visited.add((i, j))
            for x in range(len(rows)):
                maxgold = max(
                    maxgold, 
                dfs(grid, i + rows[x], j + cols[x], visited)
                )
            visited.remove((i,j))
            return maxgold + grid[i][j]
            
        maxgold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    visited = set()
                    maxgold = max(maxgold, dfs(grid, i, j, visited))
        
        return maxgold
    
