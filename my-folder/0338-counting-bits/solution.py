class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        for i in range(n+1):
            bin_str = bin(i)
            ans.append(bin_str.count('1'))
        
        return ans
