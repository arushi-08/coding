class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left = 0
        right = len(nums)-1
        
        while(left + 1 < right):
            mid = (left + right)//2
                
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
                
        if left + 1 == right:
            if nums[left] > nums[left + 1]:
                return left
            else:
                return left + 1
        
        return left
