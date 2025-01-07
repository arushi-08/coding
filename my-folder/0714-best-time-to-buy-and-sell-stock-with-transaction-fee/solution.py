class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # current day transaction has 3 ops: buy, sell, nothing/free
        # current day maxprofit depends on previos maxprofit + current transactions
        # but current transactions depends on whether we bought or sold in previous days
        # so keep 2 dp arrays
        # 1 calculates maxprofit when we are not holding stock (sell, free)
        # other calculates maxprofit when we are holding stock (buy, free)
        hold_profit = -prices[0]
        free_profit = 0

        for i in range(1, len(prices)):
                        #  profit from holding, prev_free + profit from buying
            new_hold = max(hold_profit, free_profit - prices[i])
                        # prev free profit, selling prev hold at current price
            new_free = max(free_profit, prices[i] + hold_profit - fee)
            hold_profit, free_profit = new_hold, new_free
        
        return free_profit
