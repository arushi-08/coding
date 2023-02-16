class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(','{','[']:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if stack[-1]+s[i] in ['{}','()','[]']:
                    stack.pop()
                    continue
                return False
        
        if not stack:
            return True
        return False
                
