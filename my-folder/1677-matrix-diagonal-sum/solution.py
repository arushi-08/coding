class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        r = len(mat)
        c = len(mat[0])
        diagsum = 0
        for i in range(r):
            if (i,i) != (i,c-i-1):
                diagsum += mat[i][i] + mat[i][c-i-1]
            else:
                diagsum += mat[i][i]
        
        return diagsum
