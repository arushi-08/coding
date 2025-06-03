class Solution:
    def isHappy(self, n: int) -> bool:

        def next_val(n):
            nextn = 0

            while n:
                n, rem = divmod(n, 10)
                nextn += rem ** 2

            return nextn

        
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = next_val(n)
            
        
        return n == 1

