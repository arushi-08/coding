class Solution:
    def reverseWords(self, s: str) -> str:
        
        slist = s.strip().split()

        return ' '.join(slist[::-1])
