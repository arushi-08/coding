class Solution:
    def __init__(self):
        self.dir_rows = [1, 0, -1, 0]
        self.dir_cols = [0, 1, 0, -1]
        self.n_dirs = len(self.dir_rows)

    def numIslands(self, grid: List[List[str]]) -> int:
        
        "count num of islands, bfs"
        n_rows = len(grid)
        n_cols = len(grid[0])

        n_islands = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    self.bfs(grid, n_rows, n_cols, i, j)
                    n_islands += 1
        return n_islands

    def bfs(self, grid, n_rows, n_cols, i, j):

        queue = deque()
        queue.append((i,j))

        while queue:
            currx, curry = queue.popleft()

            for k in range(self.n_dirs):
                
                if self.is_safe(
                    currx + self.dir_rows[k],
                    curry + self.dir_cols[k],
                    n_rows,
                    n_cols,
                    grid
                ):
                    grid[currx + self.dir_rows[k]][curry + self.dir_cols[k]] = '0'
                    queue.append(
                        (currx + self.dir_rows[k], curry + self.dir_cols[k])
                    )

    def is_safe(self, x, y, m, n, grid):

        return ( 
            0 <= x < m and 0 <= y < n and grid[x][y] == '1'
        )

