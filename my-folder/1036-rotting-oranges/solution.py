from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_oranges = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        queue.append((-1,-1))
        time = -1
        rows = [-1, 1, 0, 0]
        cols = [0, 0, -1, 1]
        while len(queue):
            curri, currj = queue.popleft()
            if curri == -1:
                time += 1
                if len(queue):
                    queue.append((-1,-1))
            else:
                for i in range(len(rows)):
                    if self.isSafe(rows[i] + curri, cols[i] + currj, grid):
                        queue.append((rows[i] + curri, cols[i] + currj))
                        grid[rows[i] + curri][cols[i] + currj] = 2
                        fresh_oranges -= 1
        return time if fresh_oranges == 0 else -1
    def isSafe(self, x, y, grid):
        return (x >= 0 and x < len(grid) and y >= 0 and y <len(grid[0]) and grid[x][y]==1)



