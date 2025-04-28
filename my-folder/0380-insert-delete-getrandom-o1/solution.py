class RandomizedSet:

    def __init__(self):
        """
        hmap = {val:idx}
        """
        self.hmap = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.hmap:
            self.hmap[val] = len(self.data)
            self.data.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        # swap elements
        """
        get idx to remove for given val from hmap
        get last_elem from data list
        place last_elem on idx to remove in data list
        
        """

        if val in self.hmap:
            idx_to_remove = self.hmap[val]
            if idx_to_remove < len(self.data)-1:
                last_elem = self.data[-1]
                self.data[idx_to_remove] = last_elem
                self.hmap[last_elem] = idx_to_remove
            self.data = self.data[:-1]
            del self.hmap[val]
            return True
        return False

    def getRandom(self) -> int:
        # each elem has same prob of being returned
        return random.choice(self.data)

# insert - {0} , [0]
# insert - {0,1}, [0,1]
# remove, 0
# insert - {0,1,2}, [0,1,2]
# remove 1
# 

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
