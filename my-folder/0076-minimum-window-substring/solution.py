from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): return ""
        # 2 pointer
        tmap = Counter(t)
        smap = {}
        st, ed = 0, 0
        minwindow = len(s)+1
        t_len = len(t)
        st_ans, ed_ans = -1,-1
        while ed < len(s):
            if s[ed] in tmap:
                if s[ed] not in smap:
                    smap[s[ed]] = 1
                    t_len -= 1
                elif smap[s[ed]] < tmap[s[ed]]:
                    smap[s[ed]] += 1
                    t_len -= 1
                else:
                    smap[s[ed]] += 1
            else:
                smap[s[ed]] = smap.get(s[ed], 0) + 1

            while t_len == 0:
                if ed - st + 1 <= minwindow:
                    st_ans = st
                    ed_ans = ed
                    minwindow = ed - st + 1
                smap[s[st]] -= 1
                
                if s[st] in tmap and smap[s[st]] < tmap[s[st]]:
                    t_len += 1

                st += 1
            ed += 1
        if st_ans == -1:
            return ""
        
        return s[st_ans:ed_ans+1]
                    
