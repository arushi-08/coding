class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        neg = False
        if s.startswith('-'):
            neg = True
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]
        
        ans = ''
        for i in range(len(s)):
            if s[i] == '0' and not ans:
                continue
            
            if s[i].isdigit():
                ans += s[i]
            else:
                break

        if not ans:
            return 0
        
        ans = int(ans)

        if neg:
            if -ans < -2**31:
                return -2**31
            return -ans

        
        if ans > (2**31)-1:
            print((2**31) - 1)
            return (2**31) - 1

        return ans
        

