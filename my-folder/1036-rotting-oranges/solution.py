class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # m x n grid
        # rotten - 2
        # fresh - 1
        # empty - 0
        # 4 directions of rotten
        # return min num of minutes
        m, n = len(grid), len(grid[0])
        n_minutes = 0
        rotten_queue = deque()
        n_fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    n_fresh += 1
                elif grid[i][j] == 2:
                    rotten_queue.append((i,j))
        
        n_rotten = len(rotten_queue)

        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        if not n_fresh: return 0
        visited = set(rotten_queue)

        while rotten_queue and n_fresh:
            n_rotten = len(rotten_queue)
            n_minutes += 1
            for i in range(n_rotten):
                x,y = rotten_queue.popleft()

                for j in range(len(rows)):
                    if self.is_fresh(x+rows[j], y+cols[j], grid, visited):
                        visited.add((x+rows[j], y+cols[j]))
                        rotten_queue.append((x+rows[j], y+cols[j]))
                        n_fresh -= 1
                        
        if n_fresh:
            return -1
        return n_minutes
    
    def is_fresh(self, x, y, grid, visited):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x,y) not in visited



