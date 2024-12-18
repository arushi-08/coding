class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        # grid given
        # amount of gold
        # start anywhere and do dfs, till you reach end
        # backtracking
        rows = [0, 1, 0, -1]
        cols = [1, 0, -1, 0]

        def dfs(grid, i, j, visited, res):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j]==0:
                return res
            
            result = 0
            for k in range(4):
                if (i+rows[k], j+cols[k]) not in visited:
                    visited.add((i+rows[k], j+cols[k]))
                    result = max(result, 
                    dfs(grid, i+rows[k], j+cols[k], 
                        visited, res+grid[i][j])
                    )
                    visited.remove((i+rows[k], j+cols[k]))
            # print('res', res + grid[i][j], i, j)
            # print('visited', visited)
            return result
        
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited.add((i,j))
                ans = max(ans, dfs(grid, i, j, visited, 0))
                visited.remove((i,j))

        return ans
