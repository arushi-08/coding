class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        """
        sarr = sort array
        when sarr and arr sums match then chunk break happens
        """
        sarr = sorted(arr)
        arrsum = 0
        sarrsum = 0
        nchunks = 0
        for i in range(len(arr)):
            arrsum += arr[i]
            sarrsum += sarr[i]
            if arrsum == sarrsum:
                nchunks += 1
        
        return nchunks

