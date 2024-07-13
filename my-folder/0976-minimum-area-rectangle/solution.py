class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        xmap = defaultdict(set)
        for point in points:
            xmap[point[0]].add(point[1])
        
        # {1:{1,3},3:{1,3},2:{2}}

        # {1:{1,3},3:{1,3},4:{1,3}}

        # find which 2 elements in hmap have 2 common items in value (y coordinate)
        # find smallest area of these 

        xmapkeys = list(xmap.keys())
        print('xmap', xmap)
        minarea = float('inf')
        for i in range(len(xmapkeys)):
            for j in range(i+1, len(xmapkeys)):
                common_ys = list(xmap[xmapkeys[i]].intersection(xmap[xmapkeys[j]]))
                if len(common_ys) >= 2:
                    mindist = float('inf')
                    for y1 in common_ys:
                        for y2 in common_ys:
                            if y1 != y2 and abs(y1-y2) < mindist:
                                mindist = abs(y1-y2)
                    minarea = min(minarea, abs(xmapkeys[j]- xmapkeys[i]) * mindist)

        return minarea if minarea != float('inf') else 0
