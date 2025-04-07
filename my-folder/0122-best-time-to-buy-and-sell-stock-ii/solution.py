class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # given prices[i]
        # 
        # can hold at most 1 stock

        max_profit = 0
        if not prices: return 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            # best time to buy and sell stock
            if buy_price < prices[i]:
                max_profit += prices[i] - buy_price
            buy_price = prices[i]
        
        return max_profit



                
