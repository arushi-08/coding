class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_to_t = {} 
        t_to_s = {}
        for i in range(len(s)):
            if s[i] in s_to_t:
                if t[i] != s_to_t[s[i]]:
                    return False
            elif t[i] in t_to_s:
                if s[i] != t_to_s[t[i]]:
                    return False
            else:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
        
        return True
