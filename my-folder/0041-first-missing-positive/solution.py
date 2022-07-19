import random
class Solution:
    def partition(self, nums, left, right):
        pivot = -1
        for j in range(len(nums)):
            if nums[j] > 0:
                pivot += 1
                nums[j], nums[pivot] = nums[pivot], nums[j]
        return pivot
        
        
    def firstMissingPositive(self, nums: List[int]) -> int:
#         use quick sort algo
#         pivot = 0
#         +ve nos will be right of pivot sort nos only in right of pivot
        lpi = self.partition(nums, 0, len(nums)-1) + 1
        for i in range(lpi):
            k = abs(nums[i])
            if k <= lpi:
                if nums[k-1] >= 0:
                    nums[k-1] = -nums[k-1]
        # print(nums)
        for i in range(lpi):
            if nums[i] > 0:
                return i + 1
        return lpi + 1
        
        
        
