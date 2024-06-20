class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        smap = Counter(s)
        for i in t:
            if i in smap:
                smap[i] -= 1
                if smap[i] == 0:
                    del smap[i]
            else:
                return i



