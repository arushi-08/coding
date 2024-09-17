from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # return numislands
        numislands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    grid[i][j] = '0'
                    self.bfs(grid, i, j) 
                    numislands += 1
        
        return numislands
    
    def bfs(self, grid, i, j):

        queue = deque()
        queue.append((i,j))

        rows = [1, 0, -1, 0]
        cols = [0, -1, 0, 1]

        while queue:
            currx, curry = queue.popleft()

            for i in range(len(rows)):
                if self.isSafe(grid, currx+rows[i], curry+cols[i]):
                    queue.append((currx+rows[i], curry+cols[i]))
                    grid[currx+rows[i]][curry+cols[i]] = '0'
    
    def isSafe(self, grid, x, y):
        return (
            x >= 0 and x < len(grid) and
            y >= 0 and y < len(grid[0]) and
            grid[x][y] == '1'
        )

