class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        maxelem = 0
        nchunks = 0
        for i in range(len(arr)):
            maxelem = max(maxelem, arr[i])
            if maxelem == i:
                nchunks += 1
        
        return nchunks
