class Solution:
    def minimumLength(self, s: str) -> int:
        
        # given s
        # chose i such that atleast 1 char to left of i i.e. = s[i] and atleast 1 char to right i.e., = s[i]
        # delete closest char to left of i = s[i]
        # remove all 3 entry chars

        # abaacbcbb
        # 012345678
        # smap[a] = [0,2,3]
        # smap[b] = [1,5,8]
        selected_idx = [1] * len(s)
        smap = defaultdict(list)
        for i in range(len(s)):
            smap[s[i]].append(i)
            if len(smap[s[i]]) == 3:
                idx1, idx2, idx3 = smap[s[i]]
                for j in (idx1, idx3):
                    selected_idx[j] = 0
                smap[s[i]] = [idx2]
        
        return selected_idx.count(1)
            



