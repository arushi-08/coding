from heapq import heappush, heappop
from collections import defaultdict
class NumberContainers:

    def __init__(self):
        self.system = defaultdict(int)
        self.system_heap = {}

    def change(self, index: int, number: int) -> None:
    
        self.system[index] = number
        if number not in self.system_heap:
            self.system_heap[number] = []
        heappush(self.system_heap[number], index)
        
        
    def find(self, number: int) -> int:
        
        if number not in self.system_heap:
            return -1
        
        while self.system_heap[number]:
            if self.system[self.system_heap[number][0]] != number: # keypoint: pop only those indices that don't point to number
                heappop(self.system_heap[number])
            else:
                return self.system_heap[number][0]
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
