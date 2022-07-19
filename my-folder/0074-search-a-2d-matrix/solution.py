class Solution:
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return self.binary_search(matrix[i], target)
        
        return False
