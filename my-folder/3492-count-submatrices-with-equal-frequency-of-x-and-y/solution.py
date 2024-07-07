class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        found_x = False
        psum = [[(0,found_x)]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                found_x = False

                if grid[i][j] == 'X':
                    newadd = 1
                elif grid[i][j] == 'Y':
                    newadd = -1
                else:
                    newadd = 0

                if j > 0 and i > 0:
                    if psum[i][j-1][1] or psum[i-1][j][1] or newadd:
                        found_x = True
                    psum[i][j] = (newadd + psum[i][j-1][0] + psum[i-1][j][0] - psum[i-1][j-1][0], found_x)
                elif j > 0:
                    if psum[i][j-1][1] or newadd:
                        found_x = True
                    psum[i][j] = (newadd + psum[i][j-1][0], found_x)
                elif i > 0:
                    if psum[i-1][j][1] or newadd:
                        found_x = True
                    psum[i][j] = (newadd + psum[i-1][j][0], found_x)
                else:
                    if newadd:
                        found_x = True
                    psum[i][j] = (newadd, found_x)

        
        ans = 0
        for i in range(row):
            for j in range(col):
                
                if psum[i][j][0] == 0 and psum[i][j][1]:
                    ans += 1

        return ans
        # x x x x 
        # x x x x
        # x x
                
        # find how many submatrices have sum of 0


