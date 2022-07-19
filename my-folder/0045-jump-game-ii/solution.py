class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0] * (len(nums)+1)
        n = len(nums)
        i = 0
        for j in range(1, n):
            while nums[i] + i < j:
                i += 1
            dp[j] = dp[i] + 1
        return dp[n-1]
            
    
    def jump_rec(self, nums):
        ans = float("inf")
        return self.helper(nums, ans)
        
    def helper(self, nums, ans):
        if not nums: return 0
        
        for i in range(1,nums[-1]):
            ans = min(self.helper(nums[:-i], ans) + 1, ans)
        
        return ans
        
