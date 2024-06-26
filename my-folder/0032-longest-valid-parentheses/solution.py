class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        arr = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and stack:
                st = stack.pop()
                arr[st] = 1
                arr[i] = 1
        
        currans = 0
        ans = 0
        for i in range(len(arr)):
            if arr[i]:
                currans += 1
            else:
                currans = 0
            ans = max(ans, currans)
                
        return ans
