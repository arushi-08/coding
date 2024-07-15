class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0]*maxSize
        self.idx = 0

    def push(self, x: int) -> None:
        if self.idx < len(self.stack):
            self.stack[self.idx] = x
            self.idx += 1

    def pop(self) -> int:
        if self.idx == 0:
            return -1
        element = self.stack[self.idx-1]
        self.stack[self.idx-1] = 0
        self.idx -= 1
        return element

    def increment(self, k: int, val: int) -> None:
        size = min(k, len(self.stack))
        for i in range(size):
            self.stack[i] += val
        



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
