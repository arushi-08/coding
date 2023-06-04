class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from each char as center, check if it can be center of a palindrome
        maxlength = 0
        def checklength(st, ed):
            ans = ''
            passonce = 0
            while st >= 0 and ed < len(s) and s[st] == s[ed]:
                st -= 1
                ed += 1
            return st+1, ed
        st, ed = 0, 0
        for i in range(len(s)):
            l, r = checklength(i, i)
            if r-l > (ed-st):
                st, ed = l, r
            l, r = checklength(i, i+1)
            if r-l > (ed-st):
                st, ed = l, r

        return s[st:ed]
            
        
