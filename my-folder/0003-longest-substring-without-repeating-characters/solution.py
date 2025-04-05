class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # given string s, find length of longest substring without duplicate chars

        # s = 'abcabcbb'
        # find length of longest substring without dups

        start = 0
        end = 0
        currset = set()
        maxlength = 0

        while end < len(s):
            # abcabcbb
            while start < end and s[end] in currset:
                currset.remove(s[start])
                start += 1
            
            currset.add(s[end])
            maxlength = max(maxlength, end - start + 1)
            end += 1
        
        return maxlength


