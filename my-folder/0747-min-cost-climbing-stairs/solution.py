class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2:
            return min(cost)
        
        dp = [0] * len(cost)
        dp[0] = 0
        dp[1] = min(cost[:2])
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-2]+cost[i-1], dp[i-1]+cost[i])
         
        return dp[-1]
