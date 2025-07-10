class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows become cols

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
           
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):

                matrix[i][j], matrix[i][len(matrix[0])-1-j] = matrix[i][len(matrix[0])-1-j], matrix[i][j]
        

