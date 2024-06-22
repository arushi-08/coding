class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        ans = []
        if n & 1 == 1:
            ans.append(0)
            n -= 1
        i = 1
        while n:
            ans = [-i] + ans + [i]
            i += 1
            n -= 2
        
        return ans
