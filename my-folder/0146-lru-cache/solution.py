class Node:
    def __init__(self, key, val=0, nextnode=None, prev=None):
        self.key = key
        self.val = val
        self.next = nextnode
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cachemap = {}
        self.cache_dll = Node(-1)
        self.tail = Node(-1)
        self.cache_dll.next = self.tail
        self.tail.prev = self.cache_dll
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cachemap:
            self.move_to_top(self.cachemap[key])
            return self.cachemap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cachemap:
            self.cachemap[key].val = value
            self.move_to_top(self.cachemap[key])
            return
        
        if self.capacity == len(self.cachemap):
            key_removed = self.get_last_removed()
            del self.cachemap[key_removed]
        
        self.cachemap[key] = Node(key, value)
        self.add(self.cachemap[key])
    
    def add(self, node):
        headnext = self.cache_dll.next
        self.cache_dll.next = node
        node.prev = self.cache_dll
        node.next = headnext
        headnext.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def move_to_top(self, node):
        self.remove(node)
        self.add(node)
    
    def get_last_removed(self):
        node_to_remove = self.tail.prev
        self.remove(node_to_remove)
        return node_to_remove.key

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
