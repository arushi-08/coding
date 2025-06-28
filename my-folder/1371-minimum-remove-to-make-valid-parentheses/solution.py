class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        if not s:
            return s
        
        res = []
        open_count = 0
        for i in range(len(s)):
            if s[i] == '(':
                open_count += 1
            elif s[i] == ')':
                open_count -= 1
            
            if open_count >= 0:
                res.append(s[i])
            else:
                open_count = 0 
        
        if open_count:
            i = len(res) - 1
            while i >= 0:
                if open_count and res[i] == '(':
                    res[i] = -1
                    open_count -= 1
                i -= 1
        return ''.join([r for r in res if r != -1])

        

                
