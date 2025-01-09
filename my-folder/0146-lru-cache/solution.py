class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key, value
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # hashmap -> o(1)
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_top(node)
            return node.val
        return -1
 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_top(node)
            return

        if len(self.cache) == self.capacity:
            lru = self.tail.prev
            if lru == self.head:
                return
            del self.cache[lru.key]
            self._remove(lru)

        self.cache[key] = Node(key, value)
        self._add_to_top(self.cache[key])

    def _remove(self, node):
        next_node = node.next
        node.prev.next = next_node
        next_node.prev = node.prev
    
    def _add_to_top(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
