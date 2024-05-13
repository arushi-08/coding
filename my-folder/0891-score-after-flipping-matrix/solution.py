class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        for i in range(len(grid)):
            if grid[i][0] == 0:
                # flip row
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                    
        # print('here 1',[row[j] for row in grid])
        
        for j in range(len(grid[0])):
            hmap = Counter([row[j] for row in grid])
            if hmap[0] > hmap[1]:
                # flip col
                for i in range(len(grid)):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        
        
        sumans = 0
        for i in range(len(grid)):
            sumans += int(''.join([str(col) for col in grid[i]]), 2)
            
        return sumans

