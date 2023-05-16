class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        start, end, ans = 0, 0, 0
        while end < len(s):
            if s[end] in hmap:
                ans = max(ans, end - start)
                while start < len(s) and hmap[s[end]] > 0:
                    hmap[s[start]] -= 1
                    start += 1
            hmap[s[end]] = 1
            end += 1
        
        return max(ans, end-start)
