class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # given string s, find length of longest substring without duplicate chars

        # s = 'abcabcbb'
        # find length of longest substring without dups

        start = 0
        end = 0
        lastseen = {}
        maxlength = 0

        for end in range(len(s)):

            if s[end] in lastseen and lastseen[s[end]] >= start:
                start = lastseen[s[end]] + 1
            
            lastseen[s[end]] = end
            maxlength = max(maxlength, end - start + 1)
        
        
        return maxlength


