class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(s.lower().split(" "))
        s = "".join([i for i in s if i.isalpha() or i.isdigit()])
        
        if not s or not s.strip():
            return True
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        # print(i, j)
        if i >= j:
            return True

        return False

