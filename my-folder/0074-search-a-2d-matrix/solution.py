class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target: return True
            if matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        row = low - 1
        if row < 0: return False
        low = 0
        high = len(matrix[0])-1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target: return True
            if matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

