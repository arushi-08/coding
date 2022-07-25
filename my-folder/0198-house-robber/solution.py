class Solution:
    def rob(self, nums: List[int]) -> int:
        # adjacent not
        # [1,2,3,1]
        # 1 + [2,3,1] 0 + [2,3,1]
        # 3 + [3,1] 1 + [3,1]  2 + [3,1] 0 + [3,1]
        # idx -> len(nums) 
        
        
        dp = [0] * (len(nums))
        
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
                continue
            if i == 1:
                dp[i] = max(nums[i], nums[i-1])
                continue
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[len(nums)-1]
