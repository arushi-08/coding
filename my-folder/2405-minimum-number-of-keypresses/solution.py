class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        i = 0
        number = 1
        press = 1
        hmap = {}
        ans = 0

        smap = Counter(s)
        stuples = sorted(smap.items(), key=lambda x:x[1], reverse=True)

        s = ''.join(char*f for char, f in stuples)
        
        while i < len(s):
            if s[i] not in hmap:
                hmap[s[i]] = press
                number += 1
                ans += press
            else:
                ans += hmap[s[i]]
                
            if number == 10:
                number = 1 
                press += 1

            i += 1
        
        return ans

