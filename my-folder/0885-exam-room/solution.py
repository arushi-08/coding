class ExamRoom:
    # [(diff, startgap, endgap), (diff2, startgap, endgap)]
    # 1000010000001
    # 2 things
    # find max dist to closest user -> midpoint of this dist return
        # for each point, calculate left distance, right distance
            # left psum -  111111222222
            # right psum - 100000
    # if user leaves, update max dist for other users
    def __init__(self, n: int):
        self.n = n
        self.heap = []
        self.heap.append((-self.dist(0,n-1), 0, n-1))

    def dist(self, l, r):
        if l == 0 or r == self.n-1:
            return r-l
        
        return (r-l)//2


    def seat(self) -> int:

        res = 0

        curr_dist, l, r = heappop(self.heap)
        curr_dist = -curr_dist
        
        if l == 0:
            res = 0
        elif r == self.n-1:
            res = self.n-1
        else:
            res = l + curr_dist

        track1, track2 = 0, 0
        if res > l:
            track1 = -self.dist(l, res-1)
            heappush(self.heap, (-self.dist(l, res-1) , l,res-1))
        if res < r:
            track2 = -self.dist(res+1, r)
            heappush(self.heap, (-self.dist(res+1, r) , res+1, r))

        print(l, r, "dist", track1, track2)
        print("res", res)
        return res

    def leave(self, p: int) -> None:
        
        previnterval, nextinterval = None, None

        for item in self.heap:
            if item[1]-1 == p:
                nextinterval = item

            elif item[2]+1 == p:
                previnterval = item
        
        start, end = p, p
        if previnterval:
            start = previnterval[1]
            self.heap.remove(previnterval)
        if nextinterval:
            end = nextinterval[2]
            self.heap.remove(nextinterval)

        heappush(self.heap, (-self.dist(start, end), start, end))

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
