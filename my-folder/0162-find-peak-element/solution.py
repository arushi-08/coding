class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left, right = 1, len(nums)
        print(nums)
        while(left < right):
            mid = (left + right) // 2
            if mid + 1 < len(nums):
                if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                    return mid
            elif mid + 1 == len(nums):
                if nums[mid-1] < nums[mid]:
                    return mid
            
            if nums[mid-1] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        
        if left == right:
            if nums[left] > nums[left - 1]:
                return left
            else:
                return left - 1
