class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # given array of interval
        # merge overlapping
        # [1,6],[8,10],[15,18]

        # (1,3) and (2,6) overlap
        # sort by start times
        # [1,5],[1,10],[2,3]

        # current interval
        # check how many next intervals overlap
        # next_start < curr_end -> overlapping
        # curr_end = max(curr_end, next_end)

        """
        compare current interval with res[-1]
        if res[-1] < st -> not overlapping -> simple append
        else overlapping -> update res[-1] = [res[-1][0] (same start), max(res[-1][1], current end) ]
        """
        if not intervals: return []

        intervals.sort()
        res = []

        for interval in intervals:
            st, ed = interval
            if res:
                prev_st, prev_ed = res[-1]
            if not res or prev_ed < st:
                res.append(interval)
            else:
                res[-1] = [prev_st, max(prev_ed, ed) ]
        
        return res

        # [[1,3],[2,6],[8,10],[15,18]]
        # curr_st = 1, curr_ed = 3
        # i = 0, j = 1
        # intervals[j][0] = 2
        # 3>2 -> overlapping
        # curr_ed = 6
        # j = 2
        # intervals[j][0] = 8
        # 3<8 -> not overlapping
        # intervals[0]= [1,6]
        # i = 2

