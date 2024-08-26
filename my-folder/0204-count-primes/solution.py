class Solution:
    def countPrimes(self, n: int) -> int:
        # sieve of eratosthenes - algo
        primes_list = [1] * n
        sqrt_n = int(n**0.5) + 1

        for i in range(2, sqrt_n):
            if primes_list[i]:
                for j in range(i*i, n, i):
                    primes_list[j] = 0
        
        return sum(primes_list[2:])



