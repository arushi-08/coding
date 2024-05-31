class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.heap = []
        self.use = defaultdict(int)
        self.counter = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.use[key] = self.counter
            self.counter += 1
            return self.cache[key]
            
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache[key] = value
            self.use[key] = self.counter
            self.counter += 1
            return

        if len(self.cache) >= self.capacity:
            while self.heap[0][0] != self.use[self.heap[0][1]]:
                _, k = heappop(self.heap)
                heappush(self.heap, (self.use[k], k))
            _, k = heappop(self.heap)
            del self.cache[k]
            del self.use[k]

        self.cache[key] = value
        self.use[key] = self.counter
        heappush(self.heap, (self.use[key], key))
        self.counter += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
