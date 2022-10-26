from heapq import heappush, heapify, heappop
class MaxStack:

    def __init__(self):
        self.stack = []
        self.stackheap = []
        self.popped = set()
        self.count = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.count))
        heappush(self.stackheap, (-x, -self.count))
        self.count += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.popped:
            self.stack.pop()
        pop, idx = self.stack.pop()
        self.popped.add(idx)
        return pop

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.popped:
            self.stack.pop()
        if self.stack:
            return self.stack[-1][0]
        return -1

    def peekMax(self) -> int:
        while self.stackheap and -self.stackheap[0][1] in self.popped:
            heappop(self.stackheap)
        if self.stackheap:
            return -self.stackheap[0][0]
        return -1
        

    def popMax(self) -> int:
        while self.stackheap and -self.stackheap[0][1] in self.popped:
            heappop(self.stackheap)
        pop, idx = heappop(self.stackheap)
        self.popped.add(-idx)
        return -pop

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
