class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        start, end = 0, 0
        max_freq = 0
        longest = 0
        while end < len(s):
            if s[end] not in hmap:
                hmap[s[end]] = 1
            else:
                hmap[s[end]] += 1
            max_freq = max(max_freq, hmap[s[end]])
            while (end - start + 1) - max_freq > k:
                longest = max(longest, end - start)
                hmap[s[start]] -= 1
                start += 1
            end += 1
        return max(longest, end-start)
