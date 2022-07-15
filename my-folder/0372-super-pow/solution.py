class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        b = int("".join([str(i) for i in b]))
        
        result = 1
        while b > 0:
            if b % 2 == 1:
                result = (result*a)%1337
            a = (a*a)%1337
            b //= 2
            
        return result%1337
