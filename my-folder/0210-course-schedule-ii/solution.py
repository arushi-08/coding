class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        # map from prereq to coureses
        prereq_to_course_map = defaultdict(list)
        course_prereq_count = {}
        for course, prereq in prerequisites:
            prereq_to_course_map[prereq].append(course)
            course_prereq_count[course] = course_prereq_count.get(course, 0) + 1
        
        result = []
        for i in range(numCourses):
            if i not in course_prereq_count:
                result.append(i)
        
        queue = deque(result)
        while queue:
            curr = queue.pop()
            for nextcourse in prereq_to_course_map[curr]:
                course_prereq_count[nextcourse] -= 1
                if course_prereq_count.get(nextcourse) == 0:
                    queue.append(nextcourse)
                    result.append(nextcourse)

        if len(result) != numCourses:
            return []
        return result


