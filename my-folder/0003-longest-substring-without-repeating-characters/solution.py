class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # given s, find length of longest substring without dup chars

        # without dups
        # abcabcbb
        # abc

        # if s[ed] == s[st]
        # move st forward
        
        st = 0
        ed = 0
        maxlen = 0
        fmap = {}

        while ed < len(s):

            while st < ed and s[ed] in fmap and fmap[s[ed]] > 0:
                fmap[ s[st] ] -= 1
                st += 1

            maxlen = max(maxlen, ed - st + 1)
            fmap[ s[ed] ] = fmap.get(s[ed], 0) + 1
            ed += 1
        
        return maxlen

