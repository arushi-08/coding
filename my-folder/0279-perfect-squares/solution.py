class Solution:
    def numSquares(self, n: int) -> int:
        
        self.memo = {}
        return self.helper(n)
    
    def helper(self, n):

        if n < 4 and n >= 0:
            return n

        if n in self.memo:
            return self.memo[n]

        i = int(n**0.5)
        ans = n
        while i > 1:
            ans = min(ans, self.helper(n - i*i) + 1)
            i -= 1

        self.memo[n] = ans
        return ans


    # def isprime(self, n):
    #     for i in range(2, int((n**0.5) + 1)):
    #         if n % i == 0:
    #             return False
    #     return True
