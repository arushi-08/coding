class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        asum = sum(aliceSizes)
        bsum = sum(bobSizes)
        bset = set(bobSizes)
        for i in range(len(aliceSizes)):
            bobreturn = aliceSizes[i] + (bsum - asum) // 2 
            if bobreturn in bset:
                return [aliceSizes[i], bobreturn]
