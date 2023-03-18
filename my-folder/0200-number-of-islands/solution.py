from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [
            [False]*len(grid[0]) for i in range(len(grid))
            ]
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=='1':
                    self.bfs(grid, i, j, visited, output)
                    output += 1
        return output

    def bfs(self, grid, i, j, visited, output):

        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        rows = [1, 0, -1, 0]
        cols = [0, 1, 0, -1]
        while len(queue):
            curri, currj = queue.popleft()
            for i in range(4):
                if self.isSafe(
                    grid, curri+rows[i],
                    currj+cols[i],visited
                    ):
                    queue.append(
                        (curri+rows[i], currj+cols[i])
                        )
                    visited[curri+rows[i]][currj+cols[i]] = True

    def isSafe(self, grid, x, y, visited):
        return (
            x >= 0 and 
            x < len(grid) and 
            y >= 0 and 
            y < len(grid[0]) and 
            not visited[x][y] and 
            grid[x][y]=='1'
            )



