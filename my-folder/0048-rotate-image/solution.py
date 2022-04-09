class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        up = 0
        down = len(matrix) - 1
        while(up < down):
            matrix[up], matrix[down] = matrix[down], matrix[up]
            up += 1
            down -= 1
        
        for i in range(len(matrix)):
            for j in range(i):
                if i!=j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                
        return matrix
