class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        st = 0
        k = 0
        for i in range(len(data)):
            if data[i]:
                k += 1
        
        kcount = 0
        minswaps = k
        for ed in range(len(data)):
            if not data[ed]:
                kcount += 1
            
            while ed - st + 1 > k: # include [st, ed] in subarray -> if this length > k
                if not data[st]:
                    kcount -= 1
                st += 1

            if ed - st + 1 == k:
                minswaps = min(minswaps, kcount)
        
        return minswaps



