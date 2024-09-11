class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        new_intervals = []
        print(intervals)
        i = 0
        # [[1,3],[2,6],[8,10],[15,18]]

        while i < len(intervals):
            sti, edi = intervals[i]
            j = i+1
            max_end = edi
            while j < len(intervals):
                # stj=2 | edj=6
                # j = 2
                stj, edj = intervals[j]
                if max_end >= stj:
                    max_end = max(max_end, edj)
                    j += 1
                else:
                    break
            # new_intervals = [[1,6],]
            # i = 2
            new_intervals.append([sti, max(max_end, intervals[j-1][1])])
            i = j
        
        return new_intervals
