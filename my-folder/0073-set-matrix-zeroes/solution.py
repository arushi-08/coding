class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # set entire row and cols to zeros
        # do in place
        m = len(matrix)
        n = len(matrix[0])
        first_row_zeros = False
        for i in range(n):
            if matrix[0][i] == 0:
                first_row_zeros = True
                break
        
        first_col_zeros = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zeros = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0

        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0
        
        if first_row_zeros:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zeros:
            for i in range(m):
                matrix[i][0] = 0

        

