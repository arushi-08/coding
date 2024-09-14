
from threading import Lock


class Node:
    def __init__(self, key=0, val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class LRUCache: 
    '''
    self.hmap:
        {key: Node(key, val, next, prev)}
    '''
    def __init__(self, capacity) -> None:
        if capacity < 0:
            raise ValueError('Capacity must be positive')
        self.capacity = capacity
        self.hmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lock = Lock()


    def get(self, key):
        with self.lock:
            if key in self.hmap:
                self._move_to_head(self.hmap[key])
                return self.hmap[key].val
            
            return -1


    def put(self, key, value):
        with self.lock:
            if key in self.hmap:
                node = self.hmap[key]
                self._move_to_head(node)
                if value != node.val:
                    self.hmap[key].val = value
                    self.head.val = value
            else:
                if len(self.hmap) == self.capacity:
                    tail = self._pop_tail()
                    del self.hmap[tail.key]
                node = Node(key=key, val=value, next=self.head)
                self.hmap[key] = node
                self._add_head(node)


    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_head(node)
        

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    

    def _pop_tail(self):
        '''
        remove node before dummy tail
        '''
        node = self.tail.prev
        if node == self.head:
            return None
        self._remove_node(node)
        return node


    def _add_head(self, node):
        '''
        add a node after dummy head
        '''
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
