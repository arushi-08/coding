class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])

        newintervals = []
        i = 0
        counter = 0
        while i < len(intervals):
            sti, edi = intervals[i]
            preved = edi
            j = i + 1
            while j < len(intervals):
                stj, edj = intervals[j]
                if stj <= preved:
                    preved = max(preved, edj)
                else:
                    break
                j += 1
            
            newintervals.append([sti, preved])
            i = j

        return newintervals
