class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n in range(3):
            return n
        dp = [0] * (n + 1)
        for i in range(3):
            dp[i] = i
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
