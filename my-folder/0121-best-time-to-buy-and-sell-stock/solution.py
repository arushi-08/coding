from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_val = 0
        max_profit = 0
        for i in range(len(prices)):
            min_val = min(min_val, prices[i])
            max_profit = max(prices[i] - min_val, max_profit)

        return max_profit
