class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        # meeting will take place in the unused room with lowest number
        # if no available rooms, meeting is delayed until a room becomes free
        # delayed meeting should have same duration as original meeting
        # when room becomes unused, meetings with earlier original start time should be given

        # return number of room that held the most meetings,
        # if multiple, return smallest

        # rooms_heap = [(0,end_time)]
        
        # for meeting on meetings:
        #   if meeting[0] > rooms_heap[0][1]:
        #       rooms_heap[0][1] = meeting[1]
        #       count_meetings[rooms_heap[0]] += 1
        #   else:
        #       overlapping, find another room from rooms_heap
        #       
        # 

        """
        Use List<Heap> rooms containing meeting end times
        iterate on rooms

        """

        meetings.sort()
        print('meetings', meetings)
        rooms = [[] for _ in range(n)]

        for meeting in meetings:
            placed = False
            next_room = None
            min_end_time_curr_meetings = float('inf')

            for room in rooms:
                if not room or -room[0] <= meeting[0]:
                    heappush(room, -meeting[1])
                    placed = True
                    break
                
                if -room[0] < min_end_time_curr_meetings:
                    min_end_time_curr_meetings = -room[0]
                    next_room = room
            
            if not placed:
                heappush(next_room, -((meeting[1] - meeting[0]) - next_room[0]))
                
        print('rooms', rooms)
        max_meetings = 0
        room_num = 0
        for i, room in enumerate(rooms):
            if max_meetings < len(room):
                room_num = i
                max_meetings = len(room)
        
        return room_num

# [[0,10],[1,5],[2,7],[3,4]]
# meeting = [0,10]
# rooms = [[10], ..]

# meeting = [1,5]
# rooms = [[10], [5]]
# min_end_time_curr_meetings = 5
# nextroom = [5]

# meeting = [2,7]
# rooms = [[10],[5,7]]
