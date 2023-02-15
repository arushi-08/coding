from collections import deque
class HitCounter:

    def __init__(self):
        self.counter = deque()


    def hit(self, timestamp: int) -> None:
        self.counter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # get last 300 secs hits i:i+300
        ans = 0
        i = 0
        while i < len(self.counter):
            if timestamp - self.counter[i] < 300:
                ans += 1
                i += 1
            else:
                self.counter.popleft()
        return ans

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
