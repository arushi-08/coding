class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = {}
        for i in range(len(points)):
            dist[(i, points[i][0], points[i][1])] = pow(points[i][0]**2 + points[i][1]**2, 0.5)
        # print(dist)
        dist = dict(sorted(dist.items(), key=lambda item: item[1]))
        # print(dist)
        return [[k[1], k[2]] for k in dist.keys()][:k]

            
