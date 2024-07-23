class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        open_bracket = 0

        new_s = ''
        open_bracket_idx = set()
        new_s_i = 0
        for i in s:
            if i == '(':
                open_bracket += 1

            elif i == ')':
                open_bracket -= 1
                if open_bracket_idx:
                    open_bracket_idx.pop()
            
            if open_bracket < 0:
                open_bracket = 0
            else:
                new_s += i
                if i == '(':
                    open_bracket_idx.add(new_s_i)
                new_s_i += 1
                
        ans = ''
        if open_bracket:
            for i in range(len(new_s)):
                if i not in open_bracket_idx:
                    ans += new_s[i]
        else:   
            ans = new_s

        return ans
