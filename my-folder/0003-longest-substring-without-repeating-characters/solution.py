class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding window?

        subset_map = {}
        start = 0
        maxlen = 0

        for end in range(len(s)):
            while start < end and s[end] in subset_map:
                subset_map[s[start]] -= 1
                if subset_map[s[start]] == 0:
                    del subset_map[s[start]]
                start += 1
            
            subset_map[s[end]] = subset_map.get(s[end], 0) + 1
            maxlen = max(maxlen, end - start + 1)
        
        return maxlen

