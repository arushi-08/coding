class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
#         character map to one new char
#         no 2 chars map to same char
#         char can map to itself
        
        if len(s) != len(t):
            return False
#         make counter of s and t
#         if s[i] maps to t[i], make new string
        # new_s = ''
        s_t_map = {}
        t_seen = [False]*256
        s_seen = [False]*256
        for i in range(len(s)):
            if t_seen[ord(t[i])]:
                if s_seen[ord(s[i])] and s_t_map[s[i]] == t[i]:
                    continue
                else:
                    return False
            elif not t_seen[ord(t[i])] and not s_seen[ord(s[i])]:
                    s_seen[ord(s[i])] = True
                    t_seen[ord(t[i])] = True
                    s_t_map[s[i]] = t[i]
                    continue
                
            return False
                    
                
#                 if t's ith char is already seen mapped to another s's char
#                   or s's char is already mapped to another t's char -> False
                # if s_t_map[s[i]] != t[i]:
                #     return False
                # if t[i] in s_t_map.values() and s_t_map[s[i]] != t[i]:
                
                
            
        return True
                
