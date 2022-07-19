class Solution:
    def search(self, arr: List[int], target: int) -> int:
        # if arr[left] < arr[right]:
        #:  6, 7, 0, 1, 2, 4, 5
        left = 0
        right = len(arr)-1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            # print(arr[left], arr[mid], arr[right])
            if arr[left] <= arr[mid]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
#                 right is sorted
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
    
        return -1
                
