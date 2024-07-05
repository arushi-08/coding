class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    

        s1len = len(s1)
        s2len = len(s2)

        if s1len > s2len: return False
        s1map = Counter(s1)
        s2map = Counter(s2[:s1len])
        
        for i in range(s1len, s2len):
            if s1map == s2map: 
                return True
            s2map[s2[i]] = s2map.get(s2[i], 0) + 1
            s2map[s2[i-s1len]] -= 1
            if not s2map[s2[i-s1len]]:
                del s2map[s2[i-s1len]]

        return s1map == s2map
                    
