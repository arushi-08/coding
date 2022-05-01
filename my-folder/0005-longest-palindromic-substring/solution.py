class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        ans = ""
        for i in range(len(s)):
            temp1 = self.helper(s, i, i)
            temp2 = self.helper(s, i, i+1)
            ans = max(temp1, temp2, ans, key=len)
        
        return ans
    
    def helper(self, s, l, r):
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1:r]
