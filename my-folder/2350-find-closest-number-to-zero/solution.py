class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        minval = float('inf')
        val = 0
        for i in range(len(nums)):
            if abs(nums[i]) < minval or (abs(nums[i])==minval and val < nums[i]):
                minval = abs(nums[i])
                val = nums[i]
        
        return val
