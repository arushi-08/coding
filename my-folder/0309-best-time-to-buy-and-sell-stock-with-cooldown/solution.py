class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # prices
        # find max profit i can achieve
        # complete as many transactions as i like
        # buy one and sell one share of the stock multiple times
        # cooldown one day | no consecutive sell, buy

        
        # buy, sell,
        # dp problem
        # buy, sell now, sell tomorrow
        # [1,2] -> ans : 1
        # if not bought -> if cooldown perid over (option buy), not buy
        # if bought -> options sell, not sell
        # [1,2,3] -> dp[0,1]

        profit = 0
        self.memo = {}
        return self.helper(prices, 0, -1, False, False)
    
    def helper(self, prices, i, buy, sell, cooldown):
        # [1,2,3,0,2]
        # for prices = 1, buy = 0, cooldown = 0
        #               ans = max(f([2,3,0,2, 1, 1, 0, 0]), f([2,3,0,2, 1, 0, 0, 0]))
        # 
        if i == len(prices):
            return 0
        
        if (i, buy, sell, cooldown) in self.memo:
            return self.memo[(i, buy, sell, cooldown)]

        ans = 0
        if buy == -1:
            if not cooldown:
                ans = max(self.helper(
                    prices, i+1, prices[i], sell, cooldown
                    ),
                    self.helper(
                    prices, i+1, buy, sell, cooldown
                    )
                )
            else:
                ans = self.helper(prices, i+1, buy, sell, False)
        
        else:
            ans = max(
                self.helper(
                    prices, i+1, -1, True, True
                    ) + prices[i] - buy,
                self.helper(
                    prices, i+1, buy, False, cooldown
                    )
            )

        self.memo[(i, buy, sell, cooldown)] = ans
        return ans



