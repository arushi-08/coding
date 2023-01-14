class Solution:
    def validPalindrome(self, s: str) -> bool:

        # s can be palindrome after deleting at most one character from it.
        # abacca  a a - bc -  
        i = 0
        j = len(s) - 1
        found_non_match_char = False
        non_match_idx = []
        ans = False
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                found_non_match_char = True
                if j < len(s) :
                    ans = (self.check_palindrome(s, i+1, j) | 
                    self.check_palindrome(s, i, j-1))
                break

        if ans: return True

        if not ans and not found_non_match_char: return True

        return False

    def check_palindrome(self, s, i, j):
        print(i,j,s[i:j+1])
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

        

