class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        count = 0
        for w in word:
            if w == w.upper():
                count += 1
        
        return count == len(word) or not count or (count == 1 and word[0].upper() == word[0])
