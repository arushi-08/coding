class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        
        for j in range(len(grid[0])):
            if grid[0][j]:
                # print(grid[:][j], len(grid[:][j]))
                for i in range(len(grid)):
                    grid[i][j] = 1-grid[i][j]
        
        for i in range(len(grid)):
            
            if set(grid[i]) != {0} and set(grid[i]) != {1}:
                return False
            
        return True
