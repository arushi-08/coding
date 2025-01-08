class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # longest pal substring
        longest_substr = ''
        for i in range(len(s)-1):
            substr1 = self.check_pal(s, i, i)
            substr2 = self.check_pal(s, i, i+1)
            if len(longest_substr) < len(substr1):
                longest_substr = substr1
            if len(longest_substr) < len(substr2):
                longest_substr = substr2
        
        if not longest_substr:
            return s
        return longest_substr
    
    def check_pal(self, s, st, ed):
        # cbabd
        if s[st] != s[ed]: return ''

        while st >= 0 and ed < len(s):
            if s[st] == s[ed]:
                st -= 1
                ed += 1
            else:
                break
        
        return s[st+1:ed]
