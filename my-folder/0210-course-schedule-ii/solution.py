class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq_to_course_map = defaultdict(list)
        course_to_prereq_count_map = {}

        for course, prereq in prerequisites:
            prereq_to_course_map[prereq].append(course)
            course_to_prereq_count_map[course] = course_to_prereq_count_map.get(course, 0) + 1
        
        res = []
        for i in range(numCourses):
            if i not in course_to_prereq_count_map:
                res.append(i)

        queue = deque(res)

        while queue:
            curr = queue.popleft()

            for neigh in prereq_to_course_map[curr]:
                course_to_prereq_count_map[neigh] -= 1

                if course_to_prereq_count_map[neigh] == 0:

                    res.append(neigh)
                    queue.append(neigh)
                    del course_to_prereq_count_map[neigh]
        
        if course_to_prereq_count_map == {}:
            return res
        return []

