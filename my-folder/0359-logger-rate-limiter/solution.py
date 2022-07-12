class Logger:

    def __init__(self):
        self.message_queue = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if (message in self.message_queue 
            and timestamp < self.message_queue[message] + 10):
            return False
        else:
            self.message_queue[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
