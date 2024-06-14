class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        maxheap = []
        minelem = float('inf')
        for i in range(len(nums)):
            if nums[i] & 1 != 0:
                elem = nums[i] << 1
            else:
                elem = nums[i]
            minelem = min(minelem, elem)   
            maxheap.append(-elem)

        heapify(maxheap)
        maxdiff = float('inf')

        while -maxheap[0] & 1 == 0:
            maxelem = -heappop(maxheap)
            maxdiff = min(maxdiff, maxelem - minelem)
            minelem = min(minelem, maxelem//2)
            heappush(maxheap, -maxelem//2)

        maxdiff = min(maxdiff, -maxheap[0] - minelem)
        return maxdiff
