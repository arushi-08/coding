class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if self.maxheap:
            if self.maxheap[0] <= num:
                heappush(self.minheap, -heappop(self.maxheap))
                heappush(self.maxheap, num)
            else:
                heappush(self.minheap, -num)
        else:
            heappush(self.minheap, -num)
        
        while len(self.minheap) < len(self.maxheap):
            heappush(self.minheap, -heappop(self.maxheap))
        
        while len(self.minheap) - len(self.maxheap) > 1:
            heappush(self.maxheap, -heappop(self.minheap))
        self.size += 1

    def findMedian(self) -> float:

        if self.size & 1 == 1:
            return -self.minheap[0]
            
        return (self.maxheap[0] - self.minheap[0])/2
        
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
