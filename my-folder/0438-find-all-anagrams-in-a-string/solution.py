from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        

        # return list of start idx of anagrams of p
        if len(p) > len(s): return []
        st = 0
        plen = len(p)
        pmap = [0]*26
        for i in range(plen):
            pmap[ord(p[i]) - ord('a')] += 1
        ed = len(p) - 1
        ans = []
        smap = [0]*26
        for i in range(plen):
            smap[ord(s[i]) - ord('a')] += 1

        while st < len(s):
            if smap == pmap:
                ans.append(st)
            
            smap[ord(s[st]) - ord('a')] -= 1
            # if smap[s[st]] == 0:
            #     del smap[s[st]] 
            st += 1
            ed += 1
            if ed < len(s):
                smap[ord(s[ed]) - ord('a')] += 1
            

        return ans



