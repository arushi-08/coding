class Solution:
    def __init__(self):
        self.memo = {}
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        
        
        return dp[-1] if dp[-1] < float("inf") else -1
            
        
        
#         def helper(coins, amount):
#             if amount == 0:
#                 return 0

#             if amount < 0:
#                 return float("inf")

#             if amount in self.memo:
#                 return self.memo[amount]

#             values = []
#             for i in range(len(coins)):
#                 recursion = helper(coins, amount-coins[i])
#                 # print(recursion, amount)
#                 values.append(recursion+1)

#             self.memo[amount] =  min(values)
#             return self.memo[amount]
        
#         values = helper(coins, amount)
#         return values if values < float("inf") else -1
# ----------------
#         memo = {}
        
#         def check(amount):
#             if amount in memo: return memo[amount]
#             if amount == 0: return 0
#             if amount < 0: return float("inf")
#             temp = []
#             for coin in coins:
#                 val = check(amount - coin)
#                 print(val)
#                 temp.append(1 + val)
#             memo[amount] = min(temp)
#             return memo[amount]
        
#         minimum = check(amount)
#         return minimum if minimum < float("inf") else -1

