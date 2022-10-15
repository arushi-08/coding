class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) < 3:
            return min(cost)
        
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            if i != len(cost)-1:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2] + cost[i])
        
        return dp[-1]
