class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # find min cost to climb n - 1 or n - 2
        
        if not cost: return 0
        n = len(cost)
        if n == 1: return cost[0]

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-1], dp[-2])
        
