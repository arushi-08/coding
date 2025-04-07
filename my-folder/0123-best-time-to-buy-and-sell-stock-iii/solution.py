class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # find maxprofit
        # can complete atmost 2 transactions

        # dp method
        # if not bought, either allow to buy or not allowed to buy
        # if bought, either sold or not sold
        # k times

        # 0: not bought, 1: bought
        # B S B S
        current = [0] * 5
        after = [0] * 5

        for i in range( len(prices)-1,-1,-1 ):
            for buy in range(1, 5):
                if buy % 2 == 0: # allowed to buy
                    current[buy] = max(
                        after[buy], after[buy-1] - prices[i]
                    )
                else: # buy = 2,4
                    current[buy] = max(
                        after[buy], after[buy-1] + prices[i]
                    )
            after = current[:]
        
        return after[-1]



