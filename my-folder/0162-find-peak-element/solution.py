class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        ans1 = 0
        while(left < right):
            
            mid = (left + right) // 2
            
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                if mid > 0 and nums[mid] > nums[mid - 1]:
                    return mid
                
                right = mid
            
            else:
                left = mid + 1
        
        return right
        
                
