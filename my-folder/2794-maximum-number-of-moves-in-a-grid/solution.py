class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        # start from any cell in 1st column
        # move to top right/right/bottom right cells only if their value is bigger
        # return max num of moves
        rows = [-1,0,1]
        max_moves = 0

        def is_safe(x, y, curr_val, visited):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and curr_val < grid[x][y] and (x,y) not in visited

        def dfs(curr_val, x, y, num_moves, visited):
            nonlocal max_moves
            
            if y == len(grid[0])-1:
                # print('here', num_moves)
                max_moves = max(max_moves, num_moves)
                return
            
            for i in range(len(rows)):
                # print('enter outside', x+rows[i], y+1)
                if is_safe(x+rows[i], y+1, curr_val, visited):
                    # print('enter', i, x+rows[i], y+1, grid[x+rows[i]][y+1], num_moves+1)
                    visited.add((x+rows[i], y+1))
                    dfs(grid[x+rows[i]][y+1], x+rows[i], y+1, num_moves+1, visited)
                else:
                    max_moves = max(max_moves, num_moves)

        visited = set()
        for i in range(len(grid)):
            dfs(grid[i][0], i, 0, 0, visited)
        
        return max_moves
