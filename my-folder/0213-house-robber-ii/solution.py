class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums is circular arr
        # get max value from non adj idx
        if len(nums) == 1:
            return nums[0]
        return max(
            self.helper(nums[:-1]), 
            self.helper(nums[1:])
        )
    
    def helper(self, nums):

        free = 0
        forced = 0

        for i in range(len(nums)-1,-1,-1):
            new_forced = free
            new_free = max(forced + nums[i], free)
            free, forced = new_free, new_forced
        
        return free
