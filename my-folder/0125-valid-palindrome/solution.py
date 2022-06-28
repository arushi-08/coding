import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s : return True
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
