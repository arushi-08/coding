class Solution:
    def rob(self, nums: List[int]) -> int:
        # don't take adjacent vals, maximize nums sum
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return max(dp[-1], dp[-2])
