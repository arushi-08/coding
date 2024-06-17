class MovingAverage:

    def __init__(self, size: int):
        self.window = [0] * size
        self.occupy = 0

    def next(self, val: int) -> float:
        if self.occupy == len(self.window):
            self.window.pop(0)
            self.window.append(val)
        else:
            self.window[self.occupy] = val
            self.occupy += 1

        return sum(self.window)/self.occupy


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
