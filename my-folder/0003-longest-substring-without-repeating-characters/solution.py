class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        longest = 0
        j = 1
        temp = [s[0]]
        while j < len(s):
            while s[j] in temp:
                temp.pop(0)
            temp.append(s[j])
            j += 1
            
            longest = max(longest, len(temp))
        longest = max(longest, len(temp))
        
        return longest
            
