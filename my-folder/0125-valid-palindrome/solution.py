class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [i for i in s.lower() if i.isalpha() or i.isdigit()]
        
        end_i = len(s)-1
        for i in range(len(s)):
            if s[i] != s[end_i]:
                return False
            end_i-=1
        return True
