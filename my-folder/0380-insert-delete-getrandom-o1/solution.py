class RandomizedSet:

    def __init__(self):
        self.random_hmap = {}
        self.random_list = []

    def insert(self, val: int) -> bool:
        if val not in self.random_hmap:
            self.random_hmap[val] = len(self.random_list)
            self.random_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.random_hmap:
            last_elem = self.random_list[-1]
            self.random_list[self.random_hmap[val]] = last_elem
            self.random_hmap[last_elem] = self.random_hmap[val]
            self.random_list.pop()
            del self.random_hmap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.random_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
