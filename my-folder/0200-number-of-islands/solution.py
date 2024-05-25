from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.helper(grid, visited, i, j)
                    ans += 1
        
        return ans

    def helper(self, grid, visited, i, j):
        queue = deque()
        queue.append((i,j))
        rows = [1, 0, -1, 0]
        cols = [0, -1, 0, 1]
        while queue:
            curri, currj = queue.popleft()
            for x in range(len(rows)):
                if self.isSafe(grid, visited, curri+rows[x], currj+cols[x]):
                    visited.add((curri+rows[x], currj+cols[x]))
                    queue.append((curri+rows[x], currj+cols[x]))

    def isSafe(self, grid, visited, x, y):

        return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0]) and grid[x][y] == "1" and (x,y) not in visited
