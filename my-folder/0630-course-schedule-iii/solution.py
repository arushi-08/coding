class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        

        max_duration_heap = []
        courses.sort(key=lambda x:[x[1], x[0]])
        
        curr_time = 0
        n_courses_covered = 0
        
        for i in range(len(courses)):
            if curr_time + courses[i][0] <= courses[i][1]:
                curr_time += courses[i][0]
                n_courses_covered += 1
                heappush(max_duration_heap, -courses[i][0])
            else:
                if (max_duration_heap and 
                -max_duration_heap[0] > courses[i][0]):
                    curr_time += heappop(max_duration_heap)
                    curr_time += courses[i][0]
                    heappush(max_duration_heap, -courses[i][0])
        return n_courses_covered

        # max heap
        # store min times 
        # 7, 10, 14, 19
        # 7, 3, 4, 5
        # 17,12, 18, 20
        # 10,2,4,1



# 3 - 1
# 12 - 2
# 
# 3 - 1
# 7

# 9
# 12
# 16

