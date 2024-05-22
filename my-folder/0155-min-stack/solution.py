from heapq import heappush, heapify, heappop
class MinStack:

    def __init__(self):
        self.stack = {}
        self.heap = []
        self.id = 0

    def push(self, val: int) -> None:
        self.stack[self.id] = val
        heappush(self.heap, (val, self.id))
        self.id += 1

    def pop(self) -> None:
        element = self.stack[self.id-1]
        del self.stack[self.id-1]
        # print(element, self.id,self.heap[0])
        if self.heap[0][1] == self.id-1:
            heappop(self.heap)
        self.id -= 1

    def top(self) -> int:
        return self.stack[self.id-1]

    def getMin(self) -> int:
        # {(2147483646, 1)}
        while self.heap[0][1] not in self.stack:
            heappop(self.heap)
        return self.heap[0][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
