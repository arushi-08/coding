from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = True
                    count += self.bfs(grid, i, j, visited)
        
        return count
    
    def bfs(self, grid, x, y, visited):
        q = deque()
        q.append((x, y))
        rows = [1, 0, -1, 0]
        cols = [0, -1, 0, 1]
        # ans = 0
        while q:
            curr_row, curr_col = q.popleft()
            for i in range(4):
                if self.isSafe(grid, 
                               curr_row + rows[i], 
                               curr_col + cols[i],
                               visited
                              ):
                    visited[curr_row + rows[i]][curr_col + cols[i]] = True
                    q.append((curr_row + rows[i], curr_col + cols[i]))
        return 1
    
    def isSafe(self, grid, row, col, visited):
        return (0 <= row 
                and row < len(grid) 
                and 0 <= col 
                and col < len(grid[0]) 
                and not visited[row][col]
                and grid[row][col] == "1"
               )
            
            
            
            
            
            
            
        
