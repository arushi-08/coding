class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for i in range(len(num)):
            while stack and int(stack[-1]) > int(num[i]) and k:
                stack.pop()
                k -= 1
                
            stack.append(num[i])

        if k:
            stack = stack[:-k]
        
        ans = ''.join(stack).lstrip('0') or '0'
        return ans
