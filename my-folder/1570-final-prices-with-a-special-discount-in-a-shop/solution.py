class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(prices)
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                output[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop()
            stack.append(i)

        for i in range(len(stack)):
            output[stack[i]] = prices[stack[i]]

        return output
