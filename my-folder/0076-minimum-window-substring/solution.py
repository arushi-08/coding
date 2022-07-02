from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_counter = Counter(t)
        t_len = len(t)
        i = 0
        start, end = 0, 0
        for j, char in enumerate(s, 1):
            
            if t_counter[char] > 0:
                t_len -= 1
            t_counter[char] -= 1
            
            if t_len == 0:
                while t_counter[s[i]] < 0:
                    t_counter[s[i]] += 1
                    i += 1
                    
                if end ==0 or end - start > j - i:
                    start, end = i, j
                    
                t_counter[s[i]] += 1  #why?
                t_len += 1
                i += 1
        
        return s[start:end]
        

