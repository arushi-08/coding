class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxcur = 0
        maxans = 0
        for i in range(len(nums)):
            if maxcur + nums[i]  > 0:
                maxcur += nums[i]
            else:
                maxcur = 0
            
            maxans = max(maxans, maxcur)
        
        if maxans == 0 and max(nums) < 0:
            return max(nums)
        return maxans
