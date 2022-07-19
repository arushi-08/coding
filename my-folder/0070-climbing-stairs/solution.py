class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive
#         if n < 0: return 0
#         if n <= 2: return n
        
#         return self.climbStairs(n-1) + self.climbStairs(n-2) 
        
        # n = 2 ans = 2: f(n) = f(n-1) + 1 + f(n-2) + 2
        # base condns = if n == 0 or 1 or 2: return n
        # if n == 3 return 3, 1 + 1 + 1, 2 + 1, 1 + 2
        if n <= 2: 
            return n
        
        dp = [0]*(n+1)
        for i in [0,1,2]:
            dp[i] = i
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
        
