class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        int_list = []
        
        for i in range(len(s)):
            if (ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9')) or (i==0 and s[i] in ['-', '+']):
                int_list.append(s[i])
            else:
                break
        
        uplimit = 2**31
        downlimit = -2**31
        

        if int_list in (['-'], ['+']):
            return 0
        if int_list:
            ans = int(''.join(int_list))
            if ans > uplimit - 1:
                ans = uplimit - 1
            elif ans < downlimit:
                ans = downlimit
                
            return ans
        return 0
