class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        # array of prices given
        # max profit by choosing a single day to buy 1 stock and choose next day in future to sell
        if not prices: return 0 

        profit = 0
        bought = prices[0]
        for price in prices:
            profit = max(profit, price - bought)
            bought = min(bought, price)

        return profit

