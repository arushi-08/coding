class MyQueue:

    def __init__(self):
        self.stack = []
        self.stacksize = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.stacksize += 1

    def pop(self) -> int:
        element = self.stack[0]
        if self.stacksize == 0:
            return -1
        if self.stacksize == 1:
            self.stack = []
            self.stacksize -= 1
            return element
        for i in range(1, self.stacksize):
            self.stack[i-1] = self.stack[i]
        del self.stack[self.stacksize-1]
        self.stacksize -= 1
        return element

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        if self.stacksize == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
