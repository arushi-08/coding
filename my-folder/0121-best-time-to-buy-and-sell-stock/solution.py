class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 1-buy 5-sell 3-buy 6-sell 4+3 = 
        buy = 0
        sell = 0
        profit = 0
        while sell < len(prices):
            profit = max(profit, prices[sell] - prices[buy])
            while sell > buy and prices[sell] < prices[buy]:
                buy += 1
            sell += 1
        
        return profit


