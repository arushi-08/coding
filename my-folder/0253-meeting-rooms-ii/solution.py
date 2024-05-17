from heapq import heapify, heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals: return 0

        intervals.sort(key = lambda x: x[0])

        end_time_heap = []
        heappush(end_time_heap, intervals[0][1])

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_time_heap[0]:
                heappop(end_time_heap)
            
            heappush(end_time_heap, intervals[i][1])

        return len(end_time_heap)
