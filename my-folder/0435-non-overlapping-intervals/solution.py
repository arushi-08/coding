class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # return min num of intervals needed to remove 
        
        intervals.sort(key = lambda x: x[1])
        # print(intervals)
        i = 1
        endpoint = intervals[0][1]
        remove_count = 0
        while i < len(intervals):
            if endpoint > intervals[i][0]:
                remove_count += 1
            else:
                endpoint = intervals[i][1]
            i += 1
            
        
        return remove_count
