class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        slist = s.split()
        if len(pattern) != len(slist):
            return False

        ptos = {}
        stop = {}
        for i in range(len(pattern)):
            if pattern[i] in ptos:
                if slist[i] != ptos[pattern[i]]:
                    return False
                if slist[i] in stop and stop[slist[i]] != pattern[i]:
                    return False
            elif slist[i] in stop:
                return False
            else:
                ptos[pattern[i]] = slist[i]
                stop[slist[i]] = pattern[i]
        
        return True
