class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        minsum = float('inf')
        for n in nums:
            t = n
            tempsum = 0
            while t:
                tempsum += t%10
                t //= 10
            minsum = min(minsum, tempsum)
        
        return minsum
