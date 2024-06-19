class TwoSum:

    def __init__(self):
        self.stream = []
        self.hmap = {}

    def add(self, number: int) -> None:
        self.stream.append(number)

    def find(self, value: int) -> bool:
        num = self.stream
        hmap = self.hmap
        for i in range(len(num)):
            # print(num[i], hmap)
            if num[i] in hmap:
                self.hmap = {}
                return True
            hmap[value - num[i]] = num[i]
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
