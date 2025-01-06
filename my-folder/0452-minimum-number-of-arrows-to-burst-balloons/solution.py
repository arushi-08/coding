class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # spherical balloons taped on flat wall i.e. x-y plane
        # balloons are 2d int array points
        # points[i] = [xstart, xend] -> horizontal diameter is from xstart to xend

        # return min num of arrows to burst balloons

        #         10    16
        #  2    8
        # 1   6
        #      7    12

        # sort balloons by xstart
        # (1,6) (2,8) (7,12) (10,16)

        points.sort()

        overlap_ed = points[0][1]
        num_arrows = 1
        # [[1,2],[3,4],[5,6],[7,8]]
        for i in range(len(points)):
            if overlap_ed >= points[i][0]:
                # overlap
                overlap_ed = min(overlap_ed, points[i][1])
            else:
                num_arrows += 1
                overlap_ed = points[i][1]
        
        return num_arrows

