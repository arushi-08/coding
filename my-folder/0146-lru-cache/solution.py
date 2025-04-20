import threading
class LRUCache:
    """
    how to do LRU?
        track:
            doubly LL -> push element to beg of LL
                to pop element when capacity reached in O(1)
            hashmap to get & put in cache in O(1)
    """

    def __init__(self, capacity: int):
        self.cachemap = OrderedDict()
        self.capacity = capacity
        self.lock = threading.Lock()

    def get(self, key: int) -> int:
        with self.lock:
            if key in self.cachemap:
                value = self.cachemap.pop(key)
                self.cachemap[key] = value
                return self.cachemap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        
        with self.lock:
            if key in self.cachemap:
                self.cachemap.pop(key)
            
            elif len(self.cachemap) == self.capacity:
                self.cachemap.popitem(last=False)

            self.cachemap[key] = value

    """
    How would you make your cache safe for concurrent get / put calls?


    """

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
