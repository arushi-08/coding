import math
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0
        
        ans = [1]*n
        ans[0] = 0
        ans[1] = 0
        for i in range(2, int(math.sqrt(int(n))+1)):
            
            if ans[i]:
                for j in range(i*i, n, i):
                    ans[j] = 0
                
        return sum(ans)
