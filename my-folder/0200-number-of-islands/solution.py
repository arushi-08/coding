from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # return numislands
        numislands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visited:
                    visited.add((i,j))
                    self.bfs(grid, i, j, visited)
                    numislands += 1
        
        return numislands
    
    def bfs(self, grid, i, j, visited):

        queue = deque()
        queue.append((i,j))

        rows = [1, 0, -1, 0]
        cols = [0, -1, 0, 1]

        while queue:
            currx, curry = queue.popleft()

            for i in range(len(rows)):
                if self.isSafe(grid, currx+rows[i], curry+cols[i], visited):
                    visited.add((currx+rows[i], curry+cols[i]))
                    queue.append((currx+rows[i], curry+cols[i]))
    
    def isSafe(self, grid, x, y, visited):
        return (
            x >= 0 and x < len(grid) and
            y >= 0 and y < len(grid[0]) and
            grid[x][y] == '1' and (x,y) not in visited
        )

