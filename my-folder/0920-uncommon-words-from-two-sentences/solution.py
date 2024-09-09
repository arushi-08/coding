from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        hmap = Counter(s1.split() + s2.split())
        
        uncommon_words = []
        
        for k in hmap:
            if hmap[k] == 1:
                uncommon_words.append(k)
        
        return uncommon_words
