from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # find length of longest substring without repeat
        # abcabcbb - abc - 3
        # iiii 
        # store length of abc, while left ptr reaches repeating char 1st occurence, dec local max.
        # decrease local max by 1, add 1
        # store length of bca if > abc, while left ptr reaches repeating char 1st occurence, dec local max. dec local max by 1, add 1
        # 
        window = {}
        i = 0
        j = 0
        local_max = 0
        global_max = 0
        while j < len(s):
            if s[j] in window:
                global_max = max(global_max, local_max)
                while s[j] in window:
                    del window[s[i]]
                    i += 1
                    local_max -= 1

            window[s[j]] = 1
            j += 1
            local_max += 1
        
        return max(local_max, global_max)





