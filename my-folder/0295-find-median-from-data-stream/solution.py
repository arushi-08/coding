from heapq import heappush
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.maxheap) == 0:
            heappush(self.maxheap, -num)
            return
        
        if -self.maxheap[0] > num:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            heappush(self.maxheap, -heappop(self.minheap))
        elif len(self.minheap) + 1< len(self.maxheap):
            heappush(self.minheap, -heappop(self.maxheap))
        

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            median = (self.minheap[0] - self.maxheap[0])/2
            
        elif len(self.minheap) > len(self.maxheap):
            median = self.minheap[0]
        
        else:
            median = -self.maxheap[0]
            
        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
