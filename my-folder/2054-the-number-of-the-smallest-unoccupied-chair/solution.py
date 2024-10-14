class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        # sit on smallest numbered chair
        # targetfriend = 2
        # times = [[1,4],[2,3],[4,6]]
        # 0 occupied, then 1 occupied, then 0 empty, then 0 occupied
        # keep a min heap with available seats
        # keep increasing time and see if friends arrive or leave

        # put times in heap
        # pop from heap -> smallest start time
        # assign chair
        # next pop -> compare start time with previous end time
        #           if smaller -> assign new chair
        #           else -> same chair
        # to track how long the chairs are held
        #           keep min end time
        # compare min end time (of occupied chair) with new pops
        # assign the chair to the new intervals

        times_w_frd_num = []
        friend_num = 0
        for start, end in times:
            times_w_frd_num.append((start, end, friend_num))
            friend_num += 1
        
        heapify(times_w_frd_num)

        available_chairs = list(range(len(times)))
        heapify(available_chairs)

        occupied_chairs = []
        
        while times_w_frd_num:
            start, end, friend_num = heappop(times_w_frd_num)

            while occupied_chairs and occupied_chairs[0][0] <= start:
                _, chair_num = heappop(occupied_chairs)
                heappush(available_chairs, chair_num) 
            
            if available_chairs:
                chair_num = heappop(available_chairs)
            else:
                chair_num = 0
            if friend_num == targetFriend:
                return chair_num
            heappush(occupied_chairs, (end, chair_num))
            chair_num += 1
        

            
