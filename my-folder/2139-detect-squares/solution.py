class DetectSquares:
        # count num of squares after adding points
        # know if any point is in same x (x,0), same dist y (0,x)
        # and same dist from (x,0) and (0,x) to (-x,-x) or positive coords

    def __init__(self):
        # adds new points from stream into a data structure
        self.pointscount = defaultdict(lambda : defaultdict(int))

    def add(self, point: List[int]) -> None:
        x,y = point
        self.pointscount[x][y] += 1


    def count(self, point: List[int]) -> int:
        x,y = point
        count = 0
        for cj, count_cj  in self.pointscount[x].items():
            d = abs(y-cj)
            if d == 0:
                continue
            count_a = self.pointscount[x+d][y]
            count_b = self.pointscount[x+d][cj]
            count += count_cj * count_a * count_b
            
            count_a = self.pointscount[x-d][y]
            count_b = self.pointscount[x-d][cj]
            count += count_cj * count_a * count_b

        return count    


"""

"""


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
