class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        # given 2 pos integers n and k

        # factor of n is i where n%i == 0
        # consider a list of all factors, return kth factor

        # get list of factors
        factors = []
        for i in range(1, n + 1):
            if n%i == 0:
                factors.append(i)
                if len(factors) == k:
                    return factors[-1]
        
        return -1
