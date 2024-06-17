class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        slist = s.strip().split()
        lastword = slist[-1]
        return len(lastword)
