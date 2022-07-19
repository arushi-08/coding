class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        
        if len(arr) == 1:
            return arr[0] == target
        
        left = 0
        right = len(arr) - 1
        while left <= right:
            
            while left < right and arr[left] == arr[left + 1]:
                left += 1
            while left < right and arr[right] == arr[right - 1]:
                right -= 1
            
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            
            if arr[left] <= arr[mid]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
