class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        nums[i]  amount 
            0, 1, 2, 3
         0  0  1  0. 0    1
         1  0  0  1  0    2
         2  0  0  0  0    5
        """
        
        
        dp = [[float("inf")]*(amount+1) for _ in range(len(coins))]
        
        for i in range(len(dp)):
            dp[i][0] = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if coins[i] == j:
                    dp[i][j] = 1
                
                if j >= coins[i]:
                    dp[i][j] = min(dp[i-1][j],
                                  1 + dp[i][j-coins[i]])
                else:
                    dp[i][j] = dp[i-1][j]
        
        if dp[len(coins)-1][amount] == float("inf"):
            return -1
        return dp[len(coins)-1][amount] 
        
