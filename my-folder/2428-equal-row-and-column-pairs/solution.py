class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows = []
        for i in range(len(grid)):
            rows.append(grid[i])
        
        cols = []
        for k in range(len(grid[0])):
            temp_cols = []
            for j in range(len(grid)):
                temp_cols.append(grid[j][k])
            cols.append(temp_cols)
            
        i = 0
        ans = 0
        while i < len(rows):
            j = 0
            while j < len(cols):
                if rows[i] == cols[j]:
                    ans += 1
                j += 1
            i += 1
        
        return ans
