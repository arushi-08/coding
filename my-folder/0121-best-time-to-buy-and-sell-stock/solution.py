class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprofit = 0
        minprice = float('inf')
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            if prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        
        return maxprofit
