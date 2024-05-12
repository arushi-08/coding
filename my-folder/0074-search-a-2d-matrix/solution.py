class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = 0
        # end = len(matrix[0])-1
        j = len(matrix[0])-1

        while i >= 0 and i < len(matrix) and j < len(matrix[0]) and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        
        return False
