class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 2 distinct chars
        # 2 pointers - start, end
        # move end till len(s)
        # if s[end] not in hmap - count distinct
        # if distinct count > 2:
        # move start position till distinct count drops to 2
        # store longest substring length
        hmap = {}
        start, end, distinct, longest = 0, 0, 0, 0
        while end < len(s):
            if s[end] not in hmap or hmap[s[end]] <= 0:
                distinct += 1
                while distinct > 2:
                    # if s[start] != s[end]:
                    # while hmap[s[start]] > 0 and s[start] != s[end]:
                    longest = max(longest, end-start)
                    if hmap[s[start]] == 1:
                        distinct -= 1
                    hmap[s[start]] -= 1
                    start += 1
                hmap[s[end]] = 1
            else:
                hmap[s[end]] += 1
            end += 1
        
        return max(longest, end-start)
        
