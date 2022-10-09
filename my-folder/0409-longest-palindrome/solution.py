from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        is_odd = 0
        for i in freq.values():
            if i % 2 == 0:
                ans += i
            else:
                ans += i - 1
                is_odd = 1
        
        if is_odd:
            ans += 1
        
        return ans
