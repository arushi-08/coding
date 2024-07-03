class StockSpanner:

    def __init__(self):
        self.span = []
        self.size = 0

    def next(self, price: int) -> int:

        span = 0
        
        while self.span and self.span[-1][0] <= price:
            self.span.pop()
        
        if self.span:
            last_index = self.span[-1][1]
            span = self.size - last_index

        self.span.append((price, self.size))
        self.size += 1
        
        if span:
            return span
        return self.size 


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
