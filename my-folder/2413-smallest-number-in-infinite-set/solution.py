from heapq import heappush, heappop, heapify
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1,1001))
        heapify(self.heap)
        self.present = [1]*len(list(range(1001)))
        

    def popSmallest(self) -> int:
        smallest =  heappop(self.heap)
        self.present[smallest] = 0
        return smallest

    def addBack(self, num: int) -> None:
        if self.present[num] == 0:
            heappush(self.heap, num)
            self.present[num] = 1


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
