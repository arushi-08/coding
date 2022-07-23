from heapq import heappush, heappop
class StockPrice:

    def __init__(self):
        self.records = {}
        self.maxtime = 0
        self.record_minheap = []
        self.record_maxheap = []

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price # O(1)
        self.maxtime = max(self.maxtime, timestamp)
        heappush(self.record_maxheap, (-price, timestamp))
        heappush(self.record_minheap, (price, timestamp))
        
    def current(self) -> int:
        return self.records[self.maxtime] # O(1)

    def maximum(self) -> int:
        # return max(self.records.values()) # O(N)
        
        # O(logN)
        while self.record_maxheap and -self.record_maxheap[0][0] != self.records[self.record_maxheap[0][1]]:
            popped = heappop(self.record_maxheap)
            
        if self.record_maxheap:
            return -self.record_maxheap[0][0]
        

    def minimum(self) -> int:
        # return min(self.records.values()) # O(N)
        
        # O(logN)
        while self.record_minheap and self.record_minheap[0][0] != self.records[self.record_minheap[0][1]]:
            popped = heappop(self.record_minheap)
            
        if self.record_minheap:
            return self.record_minheap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
