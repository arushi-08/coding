class Node:
    def __init__(self, key, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.size = capacity
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        
        node = self.hmap[key]
        self._remove(node)
        self._move_to_top(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self._remove(node)
            self._move_to_top(node)
        else:
            if len(self.hmap) == self.size:
                if self.tail.prev != self.head:
                    remove_node = self.tail.prev
                    self._remove(remove_node)
                    del self.hmap[remove_node.key]
            new_node = Node(key, value)
            self.hmap[key] = new_node
            self._move_to_top(new_node)


    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None
    
    def _move_to_top(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
