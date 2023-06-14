from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=='1':
                    visited[i][j] = True
                    self.bfs(grid, i, j, visited)
                    # print(i,j)
                    ans += 1
        return ans
    
    def bfs(self, grid, x, y, visited):
        queue = deque()
        queue.append((x, y))
        rows = [1, 0, -1, 0]
        cols = [0, 1, 0, -1]
        while len(queue):
            currx, curry = queue.popleft()
            for k in range(len(rows)):
                if self.isSafe(
                    grid, currx+rows[k], curry+cols[k], visited
                    ):
                    visited[currx+rows[k]][curry+cols[k]] = True
                    queue.append((currx+rows[k], curry+cols[k]))
            # print('queue',queue)
    def isSafe(self, grid, x, y, visited):
        return (x>=0 and 
        y>=0 and 
        x<len(grid) and 
        y<len(grid[0]) and 
        not visited[x][y] and 
        grid[x][y]=='1')

