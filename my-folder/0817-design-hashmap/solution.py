class Node:
    def __init__(self, key, val=0):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size_map = 1000
        self.map = [Node(-1) for _ in range(self.size_map)]

    def put(self, key: int, value: int) -> None:
        node = self.map[key % self.size_map]
        curr = node
        while curr:
            if curr.key == key:
                curr.val = value
                self.map[key % self.size_map] = node
                return
            
            if not curr.next:
                curr.next = Node(key, value)
            else:
                curr = curr.next

        self.map[key % self.size_map] = node

    def get(self, key: int) -> int:
        node = self.map[key % self.size_map]
        while node and node.key != key:
            node = node.next
        if node:
            return node.val
        return -1

    def remove(self, key: int) -> None:
        node = self.map[key % self.size_map]
        prev = node
        curr = node.next
        while curr and curr.key != key:
            curr = curr.next
            prev = prev.next

        if curr and curr.key == key:
            prev.next = curr.next

        self.map[key % self.size_map] = node


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
