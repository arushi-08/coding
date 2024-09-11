class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        
        if not self.maxheap or num <= -self.maxheap[0]:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        while len(self.maxheap)  > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        
        while len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))
        


    def findMedian(self) -> float:
        if len(self.maxheap) + len(self.minheap) & 1 == 1:
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
