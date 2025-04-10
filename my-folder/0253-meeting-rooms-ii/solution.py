class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        
        # given array of meeting time intervals
        # where intervals[i] = [starti, endi]
        # return min num of conference rooms required

        # [[0,30],[5,10],[15,20]]
        # return minimum number of conferences

        # sort - start time
        # conf can be shared - if non overlapping
        # max num of overlapping intervals at a time = num of conf rooms

        # iterate on intervals
        # if next interval start time > curr end time
        # curr meeting over -> same conf room for next
        # else: overlapping
        if not intervals: return 0

        intervals.sort()

        min_end_time_heap = []

        for interval in intervals:
            if min_end_time_heap and interval[0] >= min_end_time_heap[0]:
                
                heappop(min_end_time_heap)
            
            heappush(min_end_time_heap, interval[1])

        return len(min_end_time_heap)

        # [[7,50],[10,20],[11,40],[21,40],[42,55]]
        # min_end_time_heap = 50

        # min_end_time_heap = [20,50]
        # 
        # min_end_time_heap = [20,40,50]
        # n_conf_rooms = 1
