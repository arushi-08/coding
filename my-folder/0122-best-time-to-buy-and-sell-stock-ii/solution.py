class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this works, because we can buy and immediately sell it
        profit = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit += prices[i] - buy
            buy = prices[i]
                
            
        return profit
            
        
        
        
