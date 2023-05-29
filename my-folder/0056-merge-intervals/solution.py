class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        ans = []
        i = 1
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        while i < len(intervals):
            # curr_start = intervals[i][0]
            # curr_end = intervals[i][1]
            if curr_end < intervals[i][1]:
                if curr_end >= intervals[i][0]:
                    curr_end = intervals[i][1]
                else:
                    ans.append([curr_start, curr_end])
                    curr_start = intervals[i][0]
                    curr_end = intervals[i][1]
            i += 1
        if not ans or ans[-1] != [[curr_start, curr_end]]:
            ans.append([curr_start, curr_end])
        return ans

            

            
