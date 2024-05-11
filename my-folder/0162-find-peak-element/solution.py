class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 0
        res = -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end)//2
            print('mid', mid)
            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid
            if mid == len(nums)-1 and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if mid > 0 and nums[mid] <= nums[mid - 1]:
                end = mid - 1
            elif mid < len(nums) and nums[mid] <= nums[mid + 1]:
                start = mid + 1
        return res
