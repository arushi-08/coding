class DetectSquares:

    def __init__(self):
        self.points = []
        self.point_counts = {}

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.point_counts[tuple(point)] = self.point_counts.get(tuple(point), 0) + 1
        

    def count(self, point: List[int]) -> int:
        px,py = point
        res = 0
        for x,y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            res += self.point_counts.get((px,y), 0) * self.point_counts.get((x,py), 0)
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
