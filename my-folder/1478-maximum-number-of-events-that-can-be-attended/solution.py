from collections import defaultdict
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # need to store events based on start date
        # but attend events that end first
        # -> priority queue
        events.sort()

        heap = []
        count = 0
        i = 0
        while i < len(events) or heap:
            if not heap:
                day = events[i][0]
            
            while i < len(events) and events[i][0] == day:
                heappush(heap, events[i][1])
                i += 1
            
            heappop(heap)
            day += 1
            count += 1

            while heap and day > heap[0]:
                heappop(heap)
            
        return count
        
