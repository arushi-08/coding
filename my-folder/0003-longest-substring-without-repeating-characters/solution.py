class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        st = 0
        ed = 0
        longest_substr_length = 0
        substr_set = set()

        while ed < len(s):
            
            while st <= ed and s[ed] in substr_set:
                substr_set.remove(s[st])
                st += 1
            
            substr_set.add(s[ed])
            longest_substr_length = max(longest_substr_length, ed - st + 1)
            ed += 1
        
        return longest_substr_length

