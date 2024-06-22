class MyHashMap:

    def __init__(self):
        self.const = 1000
        self.d = [0] * (self.const + 1)

    def key(self, k):
        return divmod(k, self.const)

    def put(self, key: int, value: int) -> None:
        k1, k2 = self.key(key)
        if self.d[k1] == 0:
            self.d[k1] = [-1] * self.const
        self.d[k1][k2] = value

    def get(self, key: int) -> int:
        k1, k2 = self.key(key)
        if self.d[k1] == 0:
            return -1
        return self.d[k1][k2]

    def remove(self, key: int) -> None:
        k1, k2 = self.key(key)
        if self.d[k1] == 0:
            return
        self.d[k1][k2] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
