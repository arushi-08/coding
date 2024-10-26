class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        min_dist = float('inf')
        point_idx = -1

        for idx, point in enumerate(points):
            if point[0] == x or point[1] == y:
                if (abs(point[0] - x) + abs(point[1] - y)) < min_dist:
                    min_dist = (abs(point[0] - x) + abs(point[1] - y))
                    point_idx = idx
        
        return point_idx
