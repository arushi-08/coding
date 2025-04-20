class LogSystem:

    def __init__(self):
        self.ls = []
        # BS - find start, find end return mid
        self.granularity_map = {
            'Year' : 1,
            'Month' : 2,
            'Day': 3,
            'Hour': 4,
            'Minute': 5,
            'Second' : 6
        }

    def put(self, id: int, timestamp: str) -> None:
        bisect.insort(self.ls, (timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        "inclusive, granularity: hour, day,.."
        
        k = self.granularity_map[granularity]
        start = ':'.join(start.split(':')[:k])

        end = end.split(':')
        end = ':'.join(end[:k] + ['99'] * (6-k))
        low = (start, -float('inf'))
        high = (end, float('inf'))

        start_idx = bisect.bisect_left(self.ls, low)
        end_idx = bisect.bisect_right(self.ls, high)

        res = []
        for i in range(start_idx, end_idx):
            res.append(self.ls[i][1])
        return res
    
    
# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
