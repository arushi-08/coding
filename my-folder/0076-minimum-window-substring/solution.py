class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        st = 0
        tmap = Counter(t)
        min_length = len(s)
        min_substring = s
        tlen = len(t)
        ed = 0
        smap = {}
        st_ans, ed_ans = -1,-1

        while ed < len(s):
            if s[ed] in tmap:
                if s[ed] not in smap or smap[s[ed]] < tmap[s[ed]]:
                    smap[s[ed]] = smap.get(s[ed], 0) + 1
                    tlen -= 1 
                else:
                    smap[s[ed]] += 1
            else:
                smap[s[ed]] = smap.get(s[ed], 0) + 1

            # s='ADOBECODEBANC'
            # st = 0
            # ed = 5
            while tlen == 0:
                if min_length >= ed - st + 1:
                    st_ans = st
                    ed_ans = ed
                    min_length = ed-st+1
                smap[s[st]] -= 1
                
                if s[st] in tmap and smap[s[st]] < tmap[s[st]]:
                    tlen += 1
                
                st += 1
            
            ed += 1

        if st_ans == -1:
            return ''
        
        return s[st_ans:ed_ans+1]


                




