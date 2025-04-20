from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        """
        Pattern: 
        use key_dict {key:use}
        use defaultdict(OrderedDict) {use: OrderedDict(key:value) } = use_map
        use min_use variable

        get() - get the use of key, and update LRU info in use_map
        put() - if key in key_map, just update its use in use_map and key_map
        elif key_map has reached capacity -> pop from use_map[min_use]
                    and del key_map[min_use]
        reset min_use to 1
        and add new key
        """
        self.capacity = capacity
        self.key_map = {}
        self.use_map = defaultdict(OrderedDict)
        self.min_use = 1
        

    def get(self, key: int) -> int:
        if key in self.key_map:
            use = self.key_map[key]
            self.key_map[key] = use + 1
            val = self.use_map[use].pop(key)
            self.use_map[use+1][key] = val

            if use == self.min_use and not self.use_map[use]:
                self.min_use = use + 1
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            use = self.key_map[key]
            self.key_map[key] = use + 1
            self.use_map[use].pop(key)
            self.use_map[use+1][key] = value
            if use == self.min_use and not self.use_map[use]:
                self.min_use = use + 1

            return
        
        elif len(self.key_map) == self.capacity:
            popkey, _ = self.use_map[self.min_use].popitem(last=False)
            del self.key_map[popkey]

        self.use_map[1][key] = value
        self.key_map[key] = 1
        self.min_use = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
