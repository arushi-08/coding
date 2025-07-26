class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        

        # min conf rooms needed

        intervals.sort()
        # active smallest end time meeting
        # the max size of heap - is answer

        rooms = []
        max_rooms = 0
        for start, end in intervals:
            if rooms and rooms[0] <= start:
                # rooms stores end
                heappop(rooms)
            
            heappush(rooms, end)
            max_rooms = max(len(rooms), max_rooms)
            
        return max_rooms
