from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ran = Counter(ransomNote)
        mag = Counter(magazine)

        for k in ran.keys():
            if k in mag:
                if mag[k] >= ran[k]:
                    continue
                    
            return False
        
        return True
