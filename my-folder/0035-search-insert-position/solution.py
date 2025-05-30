class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            if nums[mid] > target:
                high = mid - 1 
            else:
                low = mid + 1
        
        return low
            
