class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        st = 0
        ed = 0
        max_count = 0
        maxlen = 0
        fmap = {}

        while ed < len(s):
            fmap[s[ed]] = fmap.get(s[ed], 0) + 1
            max_count = max(max_count, fmap[s[ed]])

            while ed - st + 1 - max_count > k:
                fmap[s[st]] -= 1
                st += 1
            
            maxlen = max(maxlen, ed - st + 1)
            ed += 1
        
        return maxlen
