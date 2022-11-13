class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n in [1,2]:
            return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,len(dp)):
            dp[i] = dp[i-1] +  dp[i-2]
        
        return dp[-1]
        
