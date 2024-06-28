class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        # make t anagram of s

        tmap = Counter(t)
        smap = Counter(s)

        # deletions = 0
        # for i in tmap:
        #     deletions += max(tmap[i] - smap.get(i, 0), 0)
        # # deletions = 1 for a (1 - 2) for b = -1 for b
        # # 
        additions = 0
        for i in smap:
            additions += max(smap[i] - tmap.get(i, 0), 0)
        
        return additions

