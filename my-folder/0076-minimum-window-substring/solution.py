from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 2 pointers + hmap
        # hmap store t freq + t_len store len(t)
        # move end to len(s)
        # if s[end] in hmap and s[end] not in smap or smap[s[end]] < hmap[s[end]]: t_len -= 1, store s[end] in smap
        # while t_len == 0: move start, store minlength 
        # remove s[start], if s[start] in smap, remove it
        if len(t) > len(s) : return ''
        start, end = 0, 0
        tmap = Counter(t)
        smap = {}
        minwindow, t_len = len(s)+1, len(t)
        start_ans, end_ans = -1,-1
        while end < len(s):
            if s[end] in tmap:
                if s[end] not in smap:
                    smap[s[end]] = 1
                    t_len -= 1
                elif smap[s[end]] < tmap[s[end]]:
                    smap[s[end]] += 1
                    t_len -= 1
                else:
                    smap[s[end]] += 1
            else:
                smap[s[end]] = smap.get(s[end], 0) + 1
            # print('outside',t_len, s[start:end+1], start)
            while t_len == 0:
                if end-start+1 <= minwindow:
                    start_ans = start
                    end_ans = end
                    minwindow = end-start+1 
                smap[s[start]] -= 1
                # print("check", s[start], smap[s[start]], tmap[s[start]])
                if s[start] in tmap and smap[s[start]] < tmap[s[start]]:
                    # print(t_len, s[start:end+1], start)
                    t_len += 1
                start += 1
            end += 1
        if start_ans == -1:
            return ''
        return s[start_ans: end_ans + 1] 
