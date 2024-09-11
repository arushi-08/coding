class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        
        n = len(haystack)
        n_needle = len(needle)

        for i in range(n - n_needle+1):
            if haystack[i:i+n_needle] == needle:
                return i
        

