class Solution:
    def findMin(self, nums: List[int]) -> int:
#         5, 1, 2, 3, 4

        if nums[0] <= nums[len(nums) - 1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        while(left < right):
            
            mid = (left + right) // 2
            
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid - 1 > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
 
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        
        return nums[left + 1]
