from collections import Counter
class Solution:

    def longestPalindrome(self, s: str) -> int:
#       abccccdd = 
        if not s: return 0
        ans = 0
        s_map = Counter(s)
        # print(s_map)
        for k, v in s_map.items():
            if v % 2 == 0:
                ans += v
            elif ans % 2 == 0:
                ans += v
            elif ans % 2 != 0:
                ans = max(ans, ans-1+v)
            print(ans, k, v)
        return ans
        


        

