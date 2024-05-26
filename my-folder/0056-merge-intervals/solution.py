class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        if not intervals: return []
        curr = 0
        remove_idx = set()
        print("intervals")
        print(intervals)
        gap = 1
        for i in range(1,len(intervals)):
            # print("curr", curr, i, intervals[curr], intervals[i])
            if intervals[curr][1] >= intervals[i][0]:
                # merge them
                intervals[curr] = [min(
                    intervals[curr][0],
                    intervals[i][0]
                ), max(
                    intervals[curr][1],
                    intervals[i][1]
                )]
                remove_idx.add(i)
                gap += 1
            else:
                curr += gap
                gap = 1
            # print("curr", curr, i, intervals[curr])
        ans = []
        for i in range(len(intervals)):
            if i in remove_idx:
                continue
            ans.append(intervals[i])
        return ans
