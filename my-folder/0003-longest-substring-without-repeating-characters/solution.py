class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        temp = [s[0]]
        j = 1
        longest = len(temp)
        
        while j < len(s):
            while s[j] in temp:
                temp.pop(0)
            temp.append(s[j])
            longest = max(longest, len(temp))
            j += 1
            
        return longest
