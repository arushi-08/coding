class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # given array of non-overlapping intervals
        # start, end of ith interval
        # insert interval
        # insert it 
        res = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]),
            max(intervals[i][1], newInterval[1])]
            i += 1
        res.append(newInterval)
       
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res

        # [[1,3],[6,9]] [2,5]
        # st=1, ed=3 | new_st=2, new_ed=5
        # 1 <= 2 <= 3 -> overlapping
        # res = [1,5]
        # [6,9]
        # not correct if new interval overlaps with next intervals
"""
    for interval in intervals:
        if not res or not overlapping:
            res.append(interval)
        else overlapping with res[-1]:
            res[-1] = [st, max_ed ]
"""     
