class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.heap = []
        heapify(self.heap)
        heappush(self.heap, (-self.nextposition(0,n-1),0,n-1))
    
    def nextposition(self, l, r):
        
        if l == 0 or r == self.n-1:
            return r - l
        return (r-l)//2

    def seat(self) -> int:

        pos, l, r = heappop(self.heap)
        pos = -pos

        res = 0
        if l == 0:
            res = l
        elif r == self.n-1:
            res = r
        else:
            res = l + pos

        if res > l:
            heappush(self.heap, (-self.nextposition(l, res-1), l, res-1))
        if res < r:
            heappush(self.heap, (-self.nextposition(res+1, r), res+1, r))

        return res
        

    def leave(self, p: int) -> None:
        previnterval, nextinterval = None, None
        item_to_remove = None
        for item in self.heap:
            pos, l, r = item
            if l == p+1:
                nextinterval = item
            if r == p-1:
                previnterval = item
        
        start = p
        end = p

        if nextinterval:
            end = nextinterval[2]
            self.heap.remove(nextinterval)
        if previnterval:
            start = previnterval[1]
            self.heap.remove(previnterval)

        heappush(self.heap, (-self.nextposition(start, end), start, end))
                


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
