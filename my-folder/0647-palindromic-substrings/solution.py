class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)):
            # aaa
            count += self.helper(s, i, i) #a
            count += self.helper(s, i, i+1) #aa
        return count
    
    def helper(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        return count
