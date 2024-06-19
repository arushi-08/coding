class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        smap = Counter(list(s))
        oddcounts = 0
        for k,v in smap.items():
            if v & 1 == 1:
                oddcounts += 1
            if oddcounts > 1:
                return False

        return True
