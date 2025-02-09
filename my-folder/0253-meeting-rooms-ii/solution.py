class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # given meeting arr where intervals[i] = [starti, endi]
        # return min num of conference rooms 

        intervals.sort()
        booked_room_endtimes = []
        heappush(booked_room_endtimes, intervals[0][1])
        
        for i in range(1, len(intervals)):

            start_x, end_x = intervals[i]
            if start_x >= booked_room_endtimes[0]:
                heappop(booked_room_endtimes)

            heappush(booked_room_endtimes, end_x)
            
        
        return len(booked_room_endtimes)
            

