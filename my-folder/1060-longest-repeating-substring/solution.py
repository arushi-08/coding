class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # 
        # 2 pointer
        # check if s[i:j] is present in s[i+1:]
        #  if true: update j+=1
        #   else: i+=1
        
        i = 0
        j = 1
        max_length = 0

        while i <= j and j < len(s):
            substr = s[i:j]
            if substr in s[i+1:]:
                j += 1
                max_length = max(max_length, len(s[i:j]))
            else:
                i += 1
            
        return max_length - 1
        






