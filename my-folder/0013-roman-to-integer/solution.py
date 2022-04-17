class Solution:
    def romanToInt(self, s: str) -> int:
        
        dict1={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        if len(s) == 1:
            return dict1[s]
        
        
        ans = 0
        skip = False
        for i in range(len(s)-1):
            if skip:
                skip = False
                continue
            print(s[i])
            if dict1[s[i]] >= dict1[s[i+1]]:
                ans += dict1[s[i]]
                print(s[i], dict1[s[i]], ans)
            
            elif dict1[s[i]] < dict1[s[i+1]]:
                ans += dict1[s[i+1]] - dict1[s[i]]
                skip = True
                print('elif',s[i], dict1[s[i]], ans)
                
        
        if len(s) >=2 and dict1[s[-2]] >= dict1[s[-1]]:
            ans += dict1[s[-1]]
        
        return ans
