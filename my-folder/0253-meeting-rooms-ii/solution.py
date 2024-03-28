class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # sort the intervals by start time
        # the intervals that overlap -> # of rooms
        
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        rooms = len(intervals)
        meeting_time = []
        for i in range(len(intervals)):
            if not meeting_time:
                meeting_time.append(intervals[i][1])
            else:
                j = 0
                while j < (len(meeting_time)):
                    if meeting_time[j] <= intervals[i][0]:
                        break
                    j += 1
                if j < len(meeting_time):
                    meeting_time[j] = intervals[i][1]
                else:
                    meeting_time.append(intervals[i][1])
        
        return len(meeting_time)

