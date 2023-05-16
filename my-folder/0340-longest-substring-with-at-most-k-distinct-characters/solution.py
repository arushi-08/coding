class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # 2 pointer - start, end
        # end moves to len(s)
        # if end not in hmap - distinct += 1
        # if distinct > k - while distinct > k 
        # if hmap[s[start]] == 1: distinct -=1
        hmap = {}
        start, end, longest, distinct = 0, 0, 0, 0
        while end < len(s):
            if s[end] not in hmap or hmap[s[end]] <= 0:
                hmap[s[end]] = 1
                distinct += 1
                while distinct > k:
                    longest = max(longest, end-start)
                    if hmap[s[start]] == 1:
                        distinct -= 1
                    hmap[s[start]] -= 1
                    start += 1
            else:
                hmap[s[end]] += 1
            end += 1
        
        return max(longest, end-start) # 6 - 2
