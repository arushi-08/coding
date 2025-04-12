class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # course schedule
        prereq_to_course_graph = defaultdict(list)
        course_to_prereq_count_map = {} 
        for course, prereq in prerequisites:
            prereq_to_course_graph[prereq].append(course)
            course_to_prereq_count_map[course] = course_to_prereq_count_map.get(course, 0) + 1
        
        queue = deque()
        for i in range(numCourses):
            if i not in course_to_prereq_count_map:
                queue.append(i)
        
        # false: cannot finish

        while queue:
            curr = queue.popleft()

            for next_course in prereq_to_course_graph[curr]:
                course_to_prereq_count_map[next_course] -= 1

                if course_to_prereq_count_map[next_course] == 0:
                    queue.append(next_course)
                    del course_to_prereq_count_map[next_course]

        return course_to_prereq_count_map == {}

