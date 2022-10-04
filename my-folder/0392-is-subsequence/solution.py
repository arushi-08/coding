from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         true -> s is subsequence of t
#         false -> otherwise
        s_map = Counter(s)
        t_map = Counter(t)
        if (len(s_map) > len(t_map) 
            or len(set(list(s_map.keys())) - set(list(t_map.keys())))!=0):
            return False
        
        j = 0
        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1
        if j >= len(s):
            return True
        return False
                
