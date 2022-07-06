from heapq import heappush, heapify
class MedianFinder:

    def __init__(self):
        self.arr = []
        self.min_heap = []
        self.max_heap = []
        self.max_size = 0
        self.min_size = 0

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 or num < -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        if len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        # print(self.max_heap, self.min_heap)
        
    def findMedian(self) -> float:
        """ 1 2 3 4    -1 -2 -3"""
        # h1 = self.arr[:(self.idx)//2]
        # h2 = self.arr[(self.idx)//2:]
        # heapify([-h for h in h1])
        # heapify(h2)
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif (len(self.max_heap) > len(self.min_heap)):
            return -self.max_heap[0]
        return self.min_heap[0]
        #     else:
                
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
