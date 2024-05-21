class Solution:
    def __init__(self):
        self.memo = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i >= coins[j]:
                    res = dp[i - coins[j]]
                    if res != -1:
                        dp[i] = min(res + 1, dp[i])

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

        # if not amount:
        #     return 0

        # if amount in self.memo:
        #     return self.memo[amount]

        # result = float('inf')
        # for i in range(len(coins)):
        #     if amount - coins[i] >= 0:
        #         res = self.coinChange(coins, amount-coins[i])
        #         if res != -1:
        #             result = min(res + 1, result)
        
        # if str(result)!='inf':
        #     self.memo[amount] = result
        # else:
        #     self.memo[amount] = -1

        # return self.memo[amount]


