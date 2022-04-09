class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        int_list = []
        
        for i in range(len(s)):
            if s[i].isdigit():
                if i > 0 and s[i-1] == "-":
                    int_list.append(s[i-1])
                int_list.append(s[i])
            
            elif not s[i].isdigit() and s[i] not in [" ", "-", "+"] and not int_list:
                    return 0
                
            if s[i] in ["-", "+"] and i + 1 < len(s) and not s[i + 1].isdigit() and not int_list:
                return 0
            
            elif int_list and not s[i].isdigit():
                break
        
        if not int_list:
            print(s)
            return 0
        
        pos = False
        
        if int_list[0].isdigit():
            pos = True
            start = 0
            count = len(int_list) - 1
        else:
            start = 1
            count = len(int_list) - 2
        ans = 0
        for i in range(start,len(int_list)):
            ans += int(int_list[i]) * pow(10, count)
            count -= 1
        
        if pos:
            if ans < pow(2,31) - 1:
                return ans
            return pow(2,31) - 1
        if -ans > pow(-2, 31):
            return -ans
        return pow(-2, 31)
            
