class LFUCache:
    # Least frequently used element popped when capacity is reached
    # element, use
    # get(): use += 1,  O(1) TC: hmap
    # put(): if new element, pop out last used, if old element, update value
    # to pop out least frequently used, track which is this
    # 5,5,5,5,5 = 5,5
    # 4,1 = 4,1
    # use counter = {element: use} {5:5, 4:1}
    # use counter is incremented when either a get or put operation is called on it

    # what is the challenge?
    # how to extract LFU element from use counter?
    # initially we have 1 element
    # when element=2, we have 2 elements with use = 1, minuse = 1
    # element = 3, minuse = 1
    # get(same element), is minuse increasing or staying same?
    # record how many elements have minuse
    # minuse = (1,3), then minuse stays same, number of elements with minuse -= 1
    # minuse = (1,2)
    # when minuse = (1,0), then update minuse, how?
    # map of use_to_elments, and iterate and see if minuse + 1, exists?

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elem_to_value_use = {}
        self.use_to_elem = defaultdict(OrderedDict)
        self.minuse = 0
        

    def get(self, key: int, new_value=0) -> int:
        if key in self.elem_to_value_use:
            value, use_times = self.elem_to_value_use[key]
            if new_value != 0:
                value = new_value
            del self.use_to_elem[use_times][key]
            if use_times == self.minuse and self.use_to_elem[self.minuse] == {}:
                del self.use_to_elem[self.minuse]
                self.minuse += 1

            self.use_to_elem[use_times+1][key] = 1
            self.elem_to_value_use[key] = [value, use_times+1]
            return value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.elem_to_value_use:
            self.get(key, value)
            return

        if len(self.elem_to_value_use) == self.capacity:
            old_key, _ = self.use_to_elem[self.minuse].popitem(last=False)
            # print('old_key', old_key)
            del self.elem_to_value_use[old_key]
            if self.use_to_elem[self.minuse] == {}:
                del self.use_to_elem[self.minuse]
                # self.minuse += 1

        self.elem_to_value_use[key] = [value, 1]
        self.use_to_elem[1][key] = 1
        self.minuse = 1
# 2,1
# 3,2
# get(3)
# get(2)
# 4,3
# get(2)
# {key: [value, use]}
# elem_to_value_use = {3:[2,2], 4:[3,1]}
# {use: keyset }
# use_to_elem = { 2:{3},1:{4} }
# minuse = 1
# get(3)
# value, use_times = 2,1
# get(2)
# value, use_times = 1,1
# old_key = 2

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
