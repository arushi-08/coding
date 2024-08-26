class Solution:

    def is_safe(self, grid, x, y, m, n):
        return (
            x < m and y < n and grid[x][y]
        )

    def dfs_can_reachable(self, grid, x, y, m, n):

        if x == m-1 and y == n-1:
            return True
        
        moves = [(0,1), (1,0)]

        for move in moves:
            i, j = move
            if self.is_safe(grid, x+i, y+j, m, n):
                if (x+i, y+j) != (m-1, n-1):
                    grid[x+i][y+j] = 0
                ans = self.dfs_can_reachable(grid, x+i, y+j, m, n)
                if ans:
                    return True
        return False

    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])

        for _ in range(2):
            ans = self.dfs_can_reachable(grid, 0, 0, m, n)
            
        if ans:
            return False
        
        return True

