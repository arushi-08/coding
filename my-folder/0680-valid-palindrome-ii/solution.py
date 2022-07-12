class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        strike_one = 0
        def verify(s, i, j, strike_one):
            
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    if strike_one:
                        return False
                    strike_one = 1
                    return verify(s, i+1, j, strike_one) or verify(s, i, j-1, strike_one)
            return True

        return verify(s, 0, len(s)-1, strike_one)
