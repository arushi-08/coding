class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.gridmap = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.gridmap[grid[i][j]]=(i,j)

    def adjacentSum(self, value: int) -> int:
        x,y = self.gridmap[value]
        adjsum = 0
        if x > 0:
            adjsum += self.grid[x-1][y]
        if y > 0:
            adjsum += self.grid[x][y-1]
        if x < len(self.grid)-1:
            adjsum += self.grid[x+1][y]
        if y < len(self.grid[0])-1:
            adjsum += self.grid[x][y+1]
        
        return adjsum

    def diagonalSum(self, value: int) -> int:
        x,y = self.gridmap[value]
        diagsum = 0
        if x > 0 and y > 0:
            diagsum += self.grid[x-1][y-1]
        if x < len(self.grid)-1 and y > 0:
            diagsum += self.grid[x+1][y-1]
        if x > 0 and y < len(self.grid[0])-1:
            diagsum += self.grid[x-1][y+1]
        if x < len(self.grid)-1 and  y < len(self.grid[0])-1:
            diagsum += self.grid[x+1][y+1]
        
        return diagsum


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
