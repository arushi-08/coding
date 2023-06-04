class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        st, ed = 0, 0
        hmap = {}
        count = 0
        maxcount = 0
        while ed < len(s):
            while s[ed] in hmap:
                del hmap[s[st]]
                st += 1
                count -= 1
            hmap[s[ed]] = 1
            count += 1
            maxcount = max(count, maxcount)
            ed += 1
        return maxcount
