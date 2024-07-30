class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        smap = {}
        st = 0
        repeat = False
        maxlength = 0
        for idx, i in enumerate(s):
            if i in smap and smap[i] == 2:
                # print('here')
                # print(s[st:idx+1], smap, i)
                smap[i] += 1
                while st < idx and smap[s[st]] != 3:
                    smap[s[st]] -= 1
                    st += 1
                if smap[s[st]] == 3:
                    smap[s[st]] -= 1
                    st += 1
            else:
                smap[i] = smap.get(i, 0) + 1
            # print(s[st:idx+1], smap, i)
            maxlength = max(maxlength, idx - st + 1)
        
        return maxlength


