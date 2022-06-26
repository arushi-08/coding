class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, i, j, visited)
                    count += 1
        return count
    
    def dfs(self, grid, i, j, visited):
        
        rows_list = [1, 0, -1, 0]
        cols_list = [0, 1, 0, -1]
        
        for k in range(4):
            if self.isSafe(grid, 
                           i + rows_list[k], 
                           j + cols_list[k], 
                           visited):
                visited[i+rows_list[k]][j+cols_list[k]] = True
                # print(visited)
                self.dfs(grid,  
                         i + rows_list[k], 
                         j + cols_list[k], 
                         visited, 
                        )
    
    def isSafe(self, grid, row, col, visited):
        # if (row < len(grid) 
                # and col < len(grid[row]) 
                # and row >= 0 
                # and col >= 0 ):
            # print(row, col, grid[row][col])
        return (row < len(grid) 
                and col < len(grid[row]) 
                and row >= 0 
                and col >= 0 
                and grid[row][col] == '1'
                and not visited[row][col]
               )



