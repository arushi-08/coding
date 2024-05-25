from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # maintain levels
        queue = deque()
        visited = set()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        queue.append((-1,0))
        rows = [1, 0, -1, 0]
        cols = [0, -1, 0, 1]
        level = -1
        while queue:

            i, j = queue.popleft()
            
            if i == -1:
                level += 1
                if queue:
                    queue.append((-1,-1))
            else:
                for x in range(len(rows)):
                    if self.isSafe(grid, i + rows[x], j + cols[x], visited):
                        queue.append((i + rows[x], j + cols[x]))
                        visited.add((i + rows[x], j + cols[x]))
                        fresh -= 1
        return level if not fresh else -1

    def isSafe(self, grid, x, y, visited):
        return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0]) and grid[x][y] == 1 and (x,y) not in visited
