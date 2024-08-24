class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # return maxprofit
        # buy - sell only 1 share at a time
        #     [7,1,5,3,6,4]
        # store ascending order in stack ,1,5,
        # when nums[i] > nums[i+1] 
        # empty stack and save stack[-1] - stack[0]

        # [7,1,5,3,6,4]
        # i=0, stack[7]
        # i=1, 7 > 1, pop from stack, profit = 0
        # 
        profit = 0
        stack = []
        for i in range(len(prices)):

            if stack and stack[-1] > prices[i]:
                maxsell = stack[-1]
                minbuy = stack[-1]
                while stack:
                    minbuy = stack.pop()
                
                profit += maxsell - minbuy

            if not stack or stack[-1] < prices[i]:
                stack.append(prices[i])
        
        if stack:
            maxsell = stack[-1]
            minbuy = stack[-1]
            while stack:
                minbuy = stack.pop()
            
            profit += maxsell - minbuy
            
        return profit
        
