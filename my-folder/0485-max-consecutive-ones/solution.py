class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxcount = max(maxcount, count)
            else:
                count = 0
        
        return maxcount
