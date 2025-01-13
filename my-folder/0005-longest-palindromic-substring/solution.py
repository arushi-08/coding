class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # dp
        # if s[i] == s[j]: 
        # babad

        # palindromic -> s[i] == s[j]
        # 

        # for each s[i] check if it's pal substr center
        max_pal_length = 1
        st, ed = 0, 0
        for i in range(len(s)-1):
            pal_length = self.get_pal_length(s, i, i)
            if max_pal_length < pal_length:
                max_pal_length = pal_length
                st, ed = i, i
            pal_length = self.get_pal_length(s, i, i+1)
            if max_pal_length < pal_length:
                max_pal_length = pal_length
                st, ed = i, i+1
        
        halflen = (max_pal_length + 1)//2
        print(max_pal_length, halflen)
        return s[st - halflen + 1 : ed + halflen]
            
    
    def get_pal_length(self, s, l, r):
        # dabac
        # 01234
        # dbc
        # 012
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        
        return r - l - 1

