class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        
        def helper(n, additive):
            nlen = len(n)

            if nlen == 0:
                return 0

            first_half = str(int(n[:(nlen//2 + nlen%2)]) + additive)

            return int(first_half + first_half[(-1-nlen%2)::-1])
        
        pals = [
            helper(n, -1), 
            helper(n, 0), 
            helper(n, 1),
            helper('9'*(len(n)-1), 0), 
            helper('1' + '0'*len(n), 0), 
            ]
        res = None
        for pal in pals:
            if str(pal) == n:
                continue

            if res is None or (abs(pal-int(n))<abs(res-int(n))) or (abs(pal-int(n))==abs(res-int(n)) and pal < res):
                res = pal
        print(pals)
        return str(res)
