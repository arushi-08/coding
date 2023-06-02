class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # use stack to get days of next warmer temperature
        # while current > stack[top] - pop top - update dist on its idx
        # push current into stack
        if not temperatures: return [0]
        stack = [(0, temperatures[0])]
        ans = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            current = temperatures[i]
            while stack and current > stack[-1][1]:
                j, _ = stack.pop() 
                ans[j] = i-j
            stack.append((i, current))
        
        return ans
