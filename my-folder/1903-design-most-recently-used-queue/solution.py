class MRUQueue:

    def __init__(self, n: int):
        self.heap = [(0,i) for i in range(1,n+1)]
        heapify(self.heap)
        self.counter = n+1

    def fetch(self, k: int) -> int:
        _, element = self.heap[k-1]
        del self.heap[k-1]
        heappush(self.heap, (self.counter, element))
        self.counter += 1
        return element


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
