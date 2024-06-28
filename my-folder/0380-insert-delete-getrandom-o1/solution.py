import random
class RandomizedSet:

    def __init__(self):
        self.hset = {}
        self.hlist = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.hset:
            return False
        self.hset[val] = self.size
        self.hlist.append(val)
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.hset:
            idx = self.hset[val]
            # print("a hlist",self.hlist, self.hset)
            last_val = self.hlist[self.size-1]
            self.hlist[idx], self.hlist[self.size-1] = self.hlist[self.size-1], self.hlist[idx]
            self.hset[last_val] = idx
            self.hlist.pop()
            self.size -= 1
            del self.hset[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.hlist)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
