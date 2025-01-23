class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        

        # each cell has value grid[i][j]
        # i.e. positive integer or -1 - blocking cell

        # can move from a non-blocked cell to another that shares an edge

        # (i,j) represent remoteness as R[i][j] which is :
        # sum of non-connected cells
        # return sum of R[i][j]

        # 1 way
        #   for each cell, get all connected cells  -> save it
        #   if not connected cell, add curr cell
        #     for each entry in connected cell list  = totalsum - connected cell sum
        #           sum it

        def dfs(i, j, visited):
            if i >= n or i < 0 or j >= n or j < 0 or (i,j) in visited or grid[i][j] == -1:
                return 0, 0

            visited.add((i,j))
            group_sum = grid[i][j]
            n_cells = 1
            for k in range(4):
                gsum, n_cell = dfs(i+rows[k], j+cols[k], visited)
                group_sum += gsum
                n_cells += n_cell
            return group_sum, n_cells

        n = len(grid)
        visited = set()
        rows = [0, 1, 0, -1]
        cols = [1, 0, -1, 0]

        total_sum = 0
        connected_cells = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    group_sum, n_cells = dfs(i, j, visited)
                    
                    connected_cells.append((group_sum, n_cells))
                    total_sum += group_sum
        
        ans = 0
        for group_sum, n_cells in connected_cells:
            ans += (total_sum - group_sum) * n_cells
    
        return ans



