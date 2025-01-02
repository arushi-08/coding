class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        p1 = 0
        p2 = 0
        i, j = 0, 0
        while p1 < len(word1) and p2 < len(word2):
            while i < len(word1[p1]) and j < len(word2[p2]):
                if word1[p1][i] != word2[p2][j]:
                    return False
                i += 1
                j += 1
            if i == len(word1[p1]):
                p1 += 1
                i = 0
            if j == len(word2[p2]):
                p2 += 1
                j = 0
        
        if p1 == len(word1) and p2 == len(word2):
            return True
        return False


