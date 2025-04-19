class Logger:

    def __init__(self):
        # each unique msg printed at most 10 seconds
        # if same msg comes within 10 seconds, drop it
        self.logmap = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logmap:
            if timestamp - self.logmap[message] < 10:
                return False
        
        self.logmap[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
