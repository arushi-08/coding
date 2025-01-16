class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        no_hold_profit = 0
        hold_profit = -prices[0]
        # [1,2,3,4,5]
        # hold_profit =   -1, -1,-1
        # no_hold_profit = 0, 0,  
        for i in range(1, len(prices)):
            # no_hold_profit - prices[i] - new hold profit, if we decide to buy at prices[i]
            # hold_profit + prices[i] - new no hold profit, if we decide to sell at prices[i]
            new_hold_profit = max(hold_profit, no_hold_profit - prices[i])
            new_no_hold_profit = max(no_hold_profit,  hold_profit + prices[i])
            hold_profit = new_hold_profit
            no_hold_profit = new_no_hold_profit

        return no_hold_profit


