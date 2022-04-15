class Solution:
        
    def rob(self, nums: List[int]) -> int:
        
        return self.rob_helper(nums, 0)
    
    def rob_helper(self, nums, i, memo={}):
        if i >= len(nums):
            return 0
        
        
        if tuple(nums[i:]) in memo:
            return memo[tuple(nums[i:])]
        
        
        memo[tuple(nums[i:])]= max(self.rob_helper(nums, i + 2) + nums[i], self.rob_helper(nums, i + 1))
        return memo[tuple(nums[i:])]
