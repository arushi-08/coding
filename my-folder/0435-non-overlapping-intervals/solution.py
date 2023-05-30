class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:x[1])
        n = len(intervals)
        count = 0
        prev = intervals[0][1]
        for i in range(1, n):
            if prev > intervals[i][0]:
                count += 1
            else:
                prev = intervals[i][1]
        return count
        
