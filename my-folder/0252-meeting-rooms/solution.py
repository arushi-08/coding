class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        

        # intervals = [start, end]

        # if person can attend all meetings

        intervals.sort()
        current_end_time = 0
        for start, end in intervals:
            if current_end_time > start:
                return False
            current_end_time = end
        
        return True
