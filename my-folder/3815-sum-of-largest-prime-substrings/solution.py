class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        # given string s, find sum of 3 largest unique prime nums
        # that can be formed using any substring

        # add next elem -> prime? -> save
                    # else move st to next elem
        p1 = []

        def isprime(candidate):
            if candidate == 1:
                return False
            if candidate in [2,3]:
                return True
            sqrt_cand = int(candidate**0.5)
            for i in range(2, sqrt_cand+1):
                if int(candidate) % i == 0:
                    return False
            return True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                candidate = int(s[i:j+1])
                if isprime(candidate):
                    if candidate in p1:
                        continue
                    if len(p1) == 3 and p1[0] < candidate:
                        heappop(p1)
                        heappush(p1, candidate)
                    elif len(p1) < 3:
                        heappush(p1, candidate)
        print(p1)
        return sum(int(i) for i in p1)
                        
                    
                    
        
