class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        # do maxpool kernel operation
        maxlocal = [[0]*(len(grid)-2)for _ in range(len(grid[0])-2)]
        
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                maxval = 0
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        maxval = max(maxval, grid[k][l])
                
                maxlocal[i][j] = maxval

        return maxlocal
