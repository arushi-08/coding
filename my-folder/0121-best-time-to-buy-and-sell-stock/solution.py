class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_ans = 0
        max_cur = 0
        for i in range(1, len(prices)):
            
            if max_cur + prices[i] - prices[i-1] > 0:
                max_cur += prices[i] - prices[i-1]
            else:
                max_cur = 0
            max_ans = max(max_ans, max_cur)
        
        return max_ans
