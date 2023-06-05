class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        st, ed = 0, 0
        hmap = {}
        max_freq = 0
        longest = 0
        while ed < len(s):
            hmap[s[ed]] = hmap.get(s[ed], 0) + 1
            max_freq = max(max_freq, hmap[s[ed]])
            while ed - st + 1 - max_freq > k:
                longest = max(longest, ed-st)
                hmap[s[st]] -= 1
                st += 1
            ed += 1
        return max(longest, ed-st)
            
