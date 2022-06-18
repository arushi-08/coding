class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        if not s: return 0
        # g.sort()
        # s.sort()
        count = 0
#         for i in range(len(g)):
#             j = 0
#             while g[i] > min(s) :
#                 s[s.index(min(s))] = float("inf")
#                 # j += 1
            
#             if g[i] < min(s):
#                 count += 1
#                 print(s)
#                 s[s.index(min(s))] = float("inf")
#                 print(s)
        
        idx_g = 0
        idx_s = 0
        g.sort()
        s.sort()
        while idx_g < len(g) and idx_s < len(s):
            if g[idx_g] > s[idx_s]:
                idx_s += 1
            else:
                count += 1
                s[idx_s] = -1
                idx_g += 1
                
        return count
