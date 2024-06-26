class Solution:
    def nearestPalindromic(self, n: str) -> str:
        

        # want same first half
        # want first half + 1
        # first half - 1
        # 9 * len_n - 1
        # 1 + 0 * len_n

        def helper(n, additive):
            nlen = len(n)
            if nlen == 0:
                return 0

            first_half = str(int(n[:(nlen//2 + nlen%2)]) + additive)
            
            return int(first_half + first_half[(-1-nlen%2)::-1])
            

        nlen = len(n)
        pal = [
            helper(n, 0),
            helper(n, 1),
            helper(n, -1),
            helper('9'*(nlen-1), 0),
            helper('1'+'0'*nlen, 0)
        ]

        res = None

        for i in pal:
            if str(i) == n:
                continue

            if res is None or abs(res - int(n)) > abs(i - int(n)) or (abs(res - int(n)) == abs(i - int(n)) and int(n) > i):
                res = i
        
        return str(res)

