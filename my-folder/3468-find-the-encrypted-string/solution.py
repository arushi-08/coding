class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        
        slist = list(s)
        n = len(s)
        for i in range(n):
            slist[i] = s[(i+k) % n]
        
        return ''.join(slist)
