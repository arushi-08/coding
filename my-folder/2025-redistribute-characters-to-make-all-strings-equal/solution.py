class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        hmap = {}
        for word in words:
            for w in word:
                hmap[w] = hmap.get(w, 0) + 1
        
        for k in hmap:
            if hmap[k] % len(words) != 0:
                return False
        
        return True

