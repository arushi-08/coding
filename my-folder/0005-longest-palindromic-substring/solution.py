class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxlength = 0
        ans = ''

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlength:
                    maxlength = r - l + 1
                    ans = s[l:r+1]
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlength:
                    maxlength = r - l + 1
                    ans = s[l:r+1]
                l -= 1
                r += 1
        
        return ans
