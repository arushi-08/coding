class RandomizedCollection:

    def __init__(self):
        self.random_hmap = {}
        self.random_list = []

    def insert(self, val: int) -> bool:
        if val not in self.random_hmap:
            self.random_hmap[val] = []
            ans = True
        else:
            ans = False
        self.random_hmap[val].append(len(self.random_list))
        self.random_list.append(val)
        return ans
# keep max idx in end of hmap value
    def remove(self, val: int) -> bool:
        if val in self.random_hmap:
            idx_list = self.random_hmap[val]
            # print('val', val)
            # print('self.random_hmap[val]', self.random_hmap[val])
            # print('self.random_list', self.random_list)
            last_element = self.random_list[-1]
            # moved last element to idx_list[-1] in random_list
            self.random_list[idx_list[-1]] = last_element
            if val != last_element:
                self.random_hmap[last_element].pop() # problem
                # popping last element
                added = False
                if self.random_hmap[last_element]:
                    for i in range(len(self.random_hmap[last_element])):
                        if self.random_hmap[last_element][i] > idx_list[-1]:
                            self.random_hmap[last_element].insert(i, idx_list[-1])
                            added = True
                            break
                if not added:
                    self.random_hmap[last_element].append(idx_list[-1])
                # print(
                #     'new self.random_hmap[last_element]', 
                #     self.random_hmap[last_element]
                # )
            self.random_hmap[val].pop()
            if not self.random_hmap[val]:
                del self.random_hmap[val]
            self.random_list.pop()
            return True
        
        return False


    def getRandom(self) -> int:
        return random.choice(self.random_list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
