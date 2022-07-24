from collections import deque
class Solution:
    def isSafe(self, x, y, n, visited, grid):
        return (x >= 0 
                and y >= 0 
                and x < n
                and y < n 
                and visited[x][y] == False 
                and grid[x][y] == 0)
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if not grid or grid[0][0] == 1: 
            return -1
        
        n = len(grid)
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        visited[0][0] = True
        
        queue = deque()
        queue.append((0,0,1))
        
        while queue:
            curr_x, curr_y, length = queue.popleft()
            print((curr_x, curr_y))
            if (curr_x, curr_y) == (n-1,n-1):
                return length
            
            possible_moves_x = [1, 1, 0, -1, -1, -1, 0, 1]
            possible_moves_y = [0, -1, -1, -1, 0, 1, 1, 1]
            
            for x, y in zip(possible_moves_x, possible_moves_y):
                if self.isSafe(curr_x+x, curr_y+y, n, visited, grid):
                    
                    visited[curr_x + x][curr_y + y] = True
                    queue.append((curr_x + x, curr_y + y, length + 1))
        
        return -1
                    
            
        
        
        
