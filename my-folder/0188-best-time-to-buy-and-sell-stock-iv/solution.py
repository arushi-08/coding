class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.memo = {}
        return self.helper(prices, 0, 1, k)
    
    def helper(self, prices, i, buy, k):

        if i == len(prices): return 0

        if k == 0: return 0

        if (i, buy, k) in self.memo: return self.memo[(i, buy, k)]

        if buy:
            self.memo[(i, buy, k)] = max(
                -prices[i] + self.helper(prices, i+1, 0, k), # buy
                0 + self.helper(prices, i+1, 1, k), # not buy
            )
        else:
            self.memo[(i, buy, k)] = max(
                prices[i] + self.helper(prices, i+1, 1, k-1),
                0 + self.helper(prices, i+1, 0, k), # not sell
            )
        return self.memo[(i, buy, k)]
